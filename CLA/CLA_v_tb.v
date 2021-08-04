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

module CLA_p_v_tb #(parameter SIZE=16);
	reg [SIZE:1] A, B;
	reg CIN;
	wire [SIZE:1] SUM;
	wire COUT;
	
	CLA_p_v #(SIZE,4) INST1(
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
		A=20'b0000000000000000; B=20'b0000000000000000; CIN=1'b0;
		#20 A=20'b00111010010111000011; B=20'b11001100101001010011; CIN=1'b0;
		#40 A=20'b10111011010011001101; B=20'b11000100010111001010; CIN=1'b1;
		#60 A=20'b00110101101011001010; B=20'b01000100101000110011; CIN=1'b1;
		end
        
endmodule
