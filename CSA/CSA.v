`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:15:56 11/01/2019 
// Design Name: 
// Module Name:    CSA top module 
// Project Name:   Carry Skip Adder
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: ADDER_SIZE must be integer multiple of GROUP_SIZE
//
//////////////////////////////////////////////////////////////////////////////////

module CSA_p #(parameter ADDER_SIZE=16, GROUP_SIZE=4)(
	output [ADDER_SIZE:1] SUM,
	output COUT,
	input [ADDER_SIZE:1] A, B,
	input CIN );

	
	wire [ADDER_SIZE/GROUP_SIZE:0] g, gp, cout;
	

        assign g[0]=CIN;

	genvar i;

		generate
			for(i=0; i<ADDER_SIZE/GROUP_SIZE; i=i+1)
				begin
					RCA_p #(GROUP_SIZE) RCAI(SUM[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], cout[i+1], A[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], B[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], g[i]);
					group_p #(GROUP_SIZE) GRPI(gp[i+1], A[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1], B[(i+1)*GROUP_SIZE:i*GROUP_SIZE+1]);
        				mux_2_input MUX2I(g[i+1], g[i], cout[i+1], gp[i+1]);					
				end
		endgenerate
      	assign COUT=g[ADDER_SIZE/GROUP_SIZE];		
endmodule
