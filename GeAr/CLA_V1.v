`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    08:36:56 30/01/2019 
// Design Name: 
// Module Name:    RCA top module 
// Project Name:   Carry Lookahead Adder
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

module CLA_p_v #(parameter SIZE=16, valency=4)(
	output [SIZE:1] SUM,
	output COUT,
	input [SIZE:1] A, B,
	input CIN
);
	wire [SIZE:0] gen, gen1;
    wire [SIZE:0] prop;
    wire [SIZE:0] p;
	wire [SIZE:0] g;

    assign gen[0]=CIN;
    assign g[0]=CIN;
	assign p[0]=0;

	genvar i, j, k;

	generate
		for(i=0; i<SIZE/valency; i=i+1) begin:CLA_Parameterized
			for(j=1; j<=valency; j=j+1) begin:CLA_bitpropgen
				BIT_G BITGEN(g[valency*i+j], A[valency*i+j], B[valency*i+j]);
				BIT_P BITPROP(p[valency*i+j], A[valency*i+j], B[valency*i+j]);
			end

			BC #(valency) BLACKCELL(
				gen1[(i+1)*valency],
				prop[(i+1)*valency],
				g[valency*(i+1):valency*i+1],
				p[valency*(i+1):valency*i+1]
			);

			GC #(2) GRAYCELL(
				gen[(i+1)*valency],
				{gen1[(i+1)*valency], gen[i*valency]},
				prop[(i+1)*valency:(i+1)*valency]
			);

			for (j=1; j<valency; j=j+1) begin:CLA_grouppropgen
				GC #(2) GRAYCELL1(
					gen[valency*i+j],
					{g[valency*i+j], gen[i*valency+j-1]},
					p[valency*i+j:valency*i+j]
				);
			end
		end

		for(k=0; k<SIZE; k=k+1)	begin:CLA_SUM
			xor g1(SUM[k+1], p[k+1], gen[k]);
		end
	endgenerate

	assign COUT=gen[SIZE];
endmodule
