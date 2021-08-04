`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:14:56 29/05/2020
// Design Name: 
// Module Name:    SARA DAR Module 
// Project Name:   Simple Accuracy-Reconfigurable Adder (SARA) Delay Adaptive Reconfigurable (DAR)
// Target Devices: 
// Tool versions: 
// Description:  SIZE: size of complete adder, groupsize: size of each SARA module, window:mux slect window
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////

module SARA_DAR_p_v #(parameter SIZE=16, groupsize=8, window=2)(
	output [SIZE:1] SUM,
	output COUT,
	input [SIZE:1] A, B,
	input CIN, 
	input carryoutselect );

	wire [SIZE:0] gen;       
        wire [SIZE:0] p;
	wire [SIZE:0] g;
     	wire [SIZE/groupsize:0] groupcarryout;
	wire [SIZE+window:1] ApproxRCON;


        assign groupcarryout[0]=CIN;
        assign gen[0]=CIN;
	assign p[0]=0;

	genvar i, j, k;


		generate 

//BIT GENERATE and BIT PROPAGATE signals
			for (i=1; i<=SIZE; i=i+1)
				begin:BIT_GENERATE_PROPAGATE
					BIT_G BITGEN(g[i],  A[i], B[i]);
					BIT_P BITPROP(p[i],  A[i], B[i]);
				end

			for (i=1; i<SIZE/groupsize; i=i+1)
				begin:EACH_GROUP
					GC #(2) GRAYCELL_GROUP(gen[(i-1)*groupsize+1], {g[(i-1)*groupsize+1], groupcarryout[i-1]}, p[(i-1)*groupsize+1]);
					for (j=1; j<groupsize; j=j+1)
						begin:RIPPLE_BLOCK
							GC #(2) GRAYCELL_GROUP(gen[(i-1)*groupsize+j+1], {g[(i-1)*groupsize+j+1], gen[(i-1)*groupsize+j]}, p[(i-1)*groupsize+j+1]);							
						end
					and (ApproxRCON[i*groupsize], p[i*groupsize+2], p[i*groupsize+1]);
					for (j=1; j<window-1; j=j+1)
						begin:PROPPAGATE_CHAIN_DETECTOR
							and (ApproxRCON[i*groupsize+j], p[i*groupsize+j+2], ApproxRCON[i*groupsize+j-1]);
						end
					mux_2_input RECON(groupcarryout[i], g[i*groupsize], gen[i*groupsize], ApproxRCON[i*groupsize+window-2]);	
				end
			GC #(2) GRAYCELL_GROUP(gen[(SIZE/groupsize-1)*groupsize+1], {g[(SIZE/groupsize-1)*groupsize+1], groupcarryout[SIZE/groupsize-1]}, p[(SIZE/groupsize-1)*groupsize+1]);
			for (j=1; j<groupsize; j=j+1)
				begin:RIPPLE_BLOCK
					GC #(2) GRAYCELL_GROUP(gen[(SIZE/groupsize-1)*groupsize+j+1], {g[(SIZE/groupsize-1)*groupsize+j+1], gen[(SIZE/groupsize-1)*groupsize+j]}, p[(SIZE/groupsize-1)*groupsize+j+1]);							
				end
			mux_2_input RECONLAST(groupcarryout[SIZE/groupsize], g[SIZE], gen[SIZE], carryoutselect);
// Generations of sum bits at every bit position	
			for(k=0; k<SIZE; k=k+1)	
				begin:CLA_SUM
					xor g1(SUM[k+1], p[k+1], gen[k]);    //SUM[i]=p[i] XOR G[i-1:0]
				end	
		endgenerate
      	assign COUT=groupcarryout[SIZE/groupsize];  //Final carry output		
endmodule
