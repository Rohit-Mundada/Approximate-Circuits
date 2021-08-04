`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    11:15:56 11/04/2019 
// Design Name: 
// Module Name:    CLA top module 
// Project Name:   Carry Lookahead Adder
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies:    Ripple Carry Adder (RCA.v), Group Propagate logic (GROUP_PROPAGATE.v), 2-input MUX (MUX_2_1.v)
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: ADDER_SIZE must be integer multiple of GROUP_SIZE
//
//////////////////////////////////////////////////////////////////////////////////

module CLA_p #(parameter ADDER_SIZE=16, GROUP_SIZE=4)(
	output [ADDER_SIZE:1] SUM,
	output COUT,
	input [ADDER_SIZE:1] A, B,
	input CIN );

	
	wire [ADDER_SIZE/GROUP_SIZE:0] g, gp, cout, gg, aout;
	

        assign g[0]=CIN;

	genvar i;

		generate
			for(i=0; i<ADDER_SIZE/GROUP_SIZE; i=i+1)
				begin
                                        group_p #((i+1)*GROUP_SIZE, i*GROUP_SIZE+1) GPRI(gp[i+1], A[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], B[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1]);
					group_g #((i+1)*GROUP_SIZE, i*GROUP_SIZE+1) GPGI(gg[i+1], A[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], B[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1]);
					RCA_p #(GROUP_SIZE) RCAI(SUM[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1],  A[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], B[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], g[i]); // Multiple ripple carry adders with size GROUP_SIZE
					and (aout[i+1], gp[i+1], g[i]);
        				or (g[i+1], aout[i+1],  gg[i+1]); 				
				end
		endgenerate
      	assign COUT=g[ADDER_SIZE/GROUP_SIZE];		
endmodule
