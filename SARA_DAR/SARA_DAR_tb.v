`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:48:56 11/01/2019 
// Design Name: 
// Module Name:    Testbench for CSA 
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

module SARA_DAR_p_tb #(parameter SIZE=16, groupsize=8, window=2);
	reg [SIZE:1] A, B;
	reg CIN;
	reg  carryoutselect;
	wire [SIZE:1] SUM;
	wire COUT;
	
	SARA_DAR_p_v #(SIZE, groupsize, window) INST1(
	.SUM(SUM),
	.COUT(COUT),
	.A(A),
	.B(B),
	.CIN(CIN),
   	.carryoutselect(carryoutselect));

	initial 
		begin
		#150 $finish;
		end

	initial
		begin
		A=16'b0000000000000000; B=16'b0000000000000000; CIN=1'b0; carryoutselect=1'b0;
		#20 A=16'b0000000111101000; B=16'b0000000001011111; CIN=1'b0; carryoutselect=1'b0;
		#40 A=16'b0000000111101000; B=16'b0000000001011111; CIN=1'b0; carryoutselect=1'b1;
		#60 A=16'b1111000111100000; B=16'b1111000000000000; CIN=1'b0; carryoutselect=1'b0;
		end
        
endmodule
