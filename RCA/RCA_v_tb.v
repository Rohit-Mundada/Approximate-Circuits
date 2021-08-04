`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    11:48:56 10/31/2019 
// Design Name: 
// Module Name:    Testbench for RCA 
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

module RCA_p_v_tb;
	reg [4:1] A, B;
	reg CIN;
	wire [4:1] SUM;
	wire COUT;
	
	RCA_p_v #(4) INST1(
	.SUM(SUM),
	.COUT(COUT),
	.A(A),
	.B(B),
	.CIN(CIN));

	initial 
		begin
		#150 $finish;
		end

	initial
		begin
		A=4'b0000; B=4'b0000; CIN=1'b0;
		#20 A=4'b0011; B=4'b1100; CIN=1'b0;
		#40 A=4'b1011; B=4'b1100; CIN=1'b1;
		#60 A=4'b0011; B=4'b0100; CIN=1'b1;
		end
        
endmodule
