`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:08:56 09/01/2020
// Design Name: 
// Module Name:    Bit generate signal
// Project Name:   Basic Components
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
module GC #(parameter valency=4)(output GG, input [valency-1 : 0] g, input [valency-1 : 1] p);

	wire [valency-1 : 0] wr, gg;

	assign gg[0]=g[0];
	

	genvar k;
	generate
	for(k=0; k<valency-1; k=k+1)
		begin
			and (wr[k], p[k+1], gg[k]);
			or (gg[k+1], wr[k], g[k+1]);                        
		end
	endgenerate	
	assign GG=gg[valency-1];
       
endmodule
