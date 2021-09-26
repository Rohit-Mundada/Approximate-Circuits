`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    08:48:56 07/05/2020
// Design Name: 
// Module Name:    RAP CLA top module 
// Project Name:   Reconfigurable Approximate Carry Look-ahead Adder (RAPCLA)
// Target Devices: 
// Tool versions: 
// Description:  SIZE: size of complete adder, groupsize: size of each RAPCLA module, window: approximation carry generation window, ApproxRCON: 1=approximate 0=exact
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////

module RAPCLA_p_v #(parameter SIZE=8, groupsize=4, window=2)(
	output [SIZE:1] SUM,
	output COUT,
	input [SIZE:1] A, B,
	input CIN );

	wire [SIZE:0] gen;       
        wire [SIZE:0] p;
	wire [SIZE:0] g;
     	wire [SIZE/groupsize:0] genexact;
	wire [2*SIZE/groupsize:1] groupgen1,groupprop1;

        assign gen[0]=CIN;
	assign p[0]=0;

	genvar i, j, k;


		generate 
			for (i=1; i<=SIZE; i=i+1)
				begin:BIT_GENERATE_PROPAGATE
					BIT_G BITGEN(g[i],  A[i], B[i]);
					BIT_P BITPROP(p[i],  A[i], B[i]);
				end

			for (i=1; i<=SIZE/groupsize; i=i+1)
				begin:BLACK_CELLS_GROUP
					BC #(groupsize-window) BLACKCELLL(groupgen1[i*2-1], groupprop1[i*2-1], g[groupsize*i-window:groupsize*(i-1)+1], p[groupsize*i-window:groupsize*(i-1)+1]); 
					BC #(window) BLACKCELLU(groupgen1[i*2], groupprop1[i*2], g[groupsize*i:groupsize*i-window+1], p[groupsize*i:groupsize*i-window+1]); 
				end

			for (i=1; i<=SIZE/groupsize; i=i+1)
				begin:SUBGROUP_END_GG
					GC #(2) GRAYCELL_LOW_GROUP(gen[i*groupsize-window], {groupgen1[i*2-1], gen[(i-1)*groupsize]}, groupprop1[i*2-1]); 
					GC #(2) GRAYCELL_HIGH_GROUP(genexact[i], {groupgen1[i*2], gen[i*groupsize-window]}, groupprop1[i*2]);
					mux_2_input RECON(gen[i*groupsize], groupgen1[i*2], genexact[i], groupgen1[i*2-1]);
					//GC #(2) GRAYCELL_LOW_GROUP_FIRST_CELL(gen[(i-1)*groupsize+1], {g[(i-1)*groupsize+1], groupcarryout[i-1]}, p[(i-1)*groupsize+1]);
					for (j=1; j<groupsize-window; j=j+1)
						begin:GROUP_GENERATE_WITHIN_LOSUBGROUP
							GC #(2) GRAYCELLLO(gen[(i-1)*groupsize+j], {g[(i-1)*groupsize+j], gen[(i-1)*groupsize+j-1]}, p[groupsize*(i-1)+j]); 
						end
					for (j=1; j<window; j=j+1)
						begin:GROUP_GENERATE_WITHIN_HIGHSUBGROUP
							GC #(2) GRAYCELLHIGH(gen[i*groupsize-window+j], {g[i*groupsize-window+j], gen[i*groupsize-window+j-1]}, p[i*groupsize-window+j]); 
						end
				end		
			for(k=0; k<SIZE; k=k+1)	
				begin:CLA_SUM
					xor g1(SUM[k+1], p[k+1], gen[k]);    //SUM[i]=p[i] XOR G[i-1:0]
				end	
		endgenerate
      	assign COUT=gen[SIZE];		
endmodule
