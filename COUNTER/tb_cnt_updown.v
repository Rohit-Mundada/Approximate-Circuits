/*
** Test bench for 32-bit updown counter	
** Author: Jinsik Yun(yun@vt.edu) 
**	   Hetaswi Vankani (hetaswi@vt.edu)  
** Last Modified : September 23, 2013
*/

`timescale 1ns/1ps

module tb_cnt_updown();
	reg	[1:0]	up_down; 
	reg		clk, reset;
	wire	[31:0]	count;

	updown_counter M1(count, up_down, clk, reset);

	initial begin
		#150 $finish;
	end

	initial begin
	end

	always begin
		#5 clk = ~clk;
	end

	initial begin
		$dumpfile ("./updown_counter.dump");
		$dumpvars (0, tb_cnt_updown);
		up_down = 2'b00; clk=0; reset=1;
		#10 reset = 0;
		#10 up_down = 2'b01;
		#60 up_down = 2'b10;
		#30 up_down = 2'b11;
		#10 reset = 1;
	end
endmodule
