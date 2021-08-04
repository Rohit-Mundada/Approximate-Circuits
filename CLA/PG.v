`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    11:48:56 10/31/2019 
// Design Name: 
// Module Name:    BIT PG & Group PG 
// Project Name:   Ripple Carry Adder
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

module BIT_PG(
	output p,
	output g,
	input a,
	input b );
	assign p = a ^ b;  // P_i=a_i XOR b_i; Propagate function 
	assign g = a & b;  // G_i=a_i AND b_i; Generate function
endmodule

module GROUP_PG(	
	output g_i_0,
	input g,
	input p,
	input g_0);	
	assign g_i_0 = g | (p & g_0); // G_i:0=G_i OR (P_i AND G_i-1:0)
endmodule
