/*
** Verilog code for 32-bit updown counter	
** Author: Jinsik Yun(yun@vt.edu) 
**	   Hetaswi Vankani (hetaswi@vt.edu)  
** Last Modified : September 23, 2013
*/

`timescale 1ns/1ps

module updown_counter ( count, up_down, clk, reset );
	output [31:0]	count;
	input [1:0] 	up_down;
  	input 			clk, reset;

	reg [31:0]	count;
	always @ (posedge clk or posedge reset)
		if (reset == 1) count <= 32'b0;
		else if (up_down == 2'b00 || up_down == 2'b11) count <= 32'b0;
		else if (up_down == 2'b01) count <= count + 1;
		else if (up_down == 2'b10) count <= count - 1;

endmodule

