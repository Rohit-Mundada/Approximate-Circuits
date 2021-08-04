`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    11:48:56 10/31/2019 
// Design Name: 
// Module Name:    RCA top module 
// Project Name:   Ripple Carry Adder
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: PG.v
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////

module RCA_p #(parameter SIZE=4)(
	output [SIZE:1] SUM,
	output COUT,
	input [SIZE:1] A, B,
	input CIN );

	wire [SIZE:0] gen;
        wire [SIZE:0] p;
	wire [SIZE:0] g;

        assign gen[0]=CIN;
        assign g[0]=CIN;

	genvar i;

		generate
			for(i=0; i<SIZE; i=i+1)
				begin:RCA_Parameterized
					BIT_PG BPG(p[i+1], g[i+1], A[i+1], B[i+1]);
					GROUP_PG GPG(gen[i+1], g[i+1], p[i+1], gen[i]);
					xor g1(SUM[i+1], p[i+1], gen[i]);
				end
		endgenerate
      	assign COUT=gen[SIZE];		
endmodule
