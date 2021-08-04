`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:15:56 11/01/2019 
// Design Name: 
// Module Name:    Group propagate signal 
// Project Name:   Carry Skip Adder
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////

module group_p #(parameter SIZE=4)(
	output GP, 
	input [SIZE:1] A, B);

	wire [SIZE:1] p;
	wire [SIZE:0] gp;   

        assign gp[0]=1;     

	genvar i;

		generate
			for(i=0; i<SIZE; i=i+1)
				begin
					xor (p[i+1], A[i+1], B[i+1]);
					and (gp[i+1], p[i+1], gp[i]);					
				end
		endgenerate
      	assign GP=gp[SIZE];		
endmodule
