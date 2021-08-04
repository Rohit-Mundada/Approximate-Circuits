`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:15:56 11/01/2019 
// Design Name: 
// Module Name:    2:1 MUX 
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

module mux_2_input (
	output OP, 
	input  A, B, sel);	 

        assign OP= (sel)? A : B;     

		
endmodule
