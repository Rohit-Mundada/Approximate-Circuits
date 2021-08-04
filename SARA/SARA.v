`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    13:14:56 07/05/2020
// Design Name: 
// Module Name:    SARA Module 
// Project Name:   Simple Accuracy-Reconfigurable Adder (SARA)
// Target Devices: 
// Tool versions: 
// Description:  SIZE: size of complete adder, groupsize: size of each SARA module
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////

module SARA_p_v #(parameter SIZE=16, groupsize=8)(
	output [SIZE:1] SUM,
	output COUT,
	input [SIZE:1] A, B,
	input CIN,
        input [SIZE/groupsize:1] ApproxRCON );

	wire [SIZE:0] gen;       
        wire [SIZE:0] p;
	wire [SIZE:0] g;
     	wire [SIZE/groupsize:0] groupcarryout;
//	wire [2*SIZE/groupsize:1] groupgen1,groupprop1;

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

			for (i=1; i<=SIZE/groupsize; i=i+1)
				begin:EACH_GROUP
					GC #(2) GRAYCELL_GROUP(gen[(i-1)*groupsize+1], {g[(i-1)*groupsize+1], groupcarryout[i-1]}, p[(i-1)*groupsize+1]);
					for (j=1; j<groupsize; j=j+1)
						begin:RIPPLE_BLOCK
							GC #(2) GRAYCELL_GROUP(gen[(i-1)*groupsize+j+1], {g[(i-1)*groupsize+j+1], gen[(i-1)*groupsize+j]}, p[(i-1)*groupsize+j+1]);							
						end
					mux_2_input RECON(groupcarryout[i], g[i*groupsize], gen[i*groupsize], ApproxRCON[i]);	
				end				
// Generations of sum bits at every bit position	
			for(k=0; k<SIZE; k=k+1)	
				begin:CLA_SUM
					xor g1(SUM[k+1], p[k+1], gen[k]);    //SUM[i]=p[i] XOR G[i-1:0]
				end	
		endgenerate
      	assign COUT=groupcarryout[SIZE/groupsize];  //Final carry output		
endmodule
