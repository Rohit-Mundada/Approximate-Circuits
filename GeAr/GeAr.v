`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    08:36:56 06/02/2020
// Design Name: 
// Module Name:    RCA top module 
// Project Name:   Generic Accuracy Configurable (GeAr) adder
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

module GeAr #(parameter N=16, R=2, P=6)(
	output [N:1] SUM,
	output COUT,
	input [N:1] A, B,
	input CIN
);
	wire [(N-R-P)/R+1:1] couti;
    wire [P:1] notused;
        
	CLA_p_v #(R+P,4) CLAINSTL(
		SUM[R+P:1], 
		couti[1], 
		A[R+P:1], 
		B[R+P:1], 
		CIN
	);

	genvar i;	

	generate
		for(i=2; i<=(N-R-P)/R+1; i=i+1) begin:GeAr_parameterized
			CLA_p_v #(R+P,4) CLAINST(
				{SUM[i*R+P:(i-1)*R+P+1], notused[P:1]}, 
				couti[i], 
				A[i*R+P:(i-1)*R+1], 
				B[i*R+P:(i-1)*R+1], 
				1'b0
			);
		end
	endgenerate

	assign COUT=couti[(N-R-P)/R+1];
endmodule
