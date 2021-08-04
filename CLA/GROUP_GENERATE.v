`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:15:56 11/03/2019 
// Design Name: 
// Module Name:    Group generate signal 
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

module group_g #(parameter i=4, j=1)(
	output GG, 	
	input [i:j] A, B);

	wire [i:j] g, p;
	wire [i:j-1] gg, gp;   

        

	genvar f;

		generate
			for(f=j; f<i+1; f=f+1)
				begin   
					if (f==j)
						and (gg[f], A[f], B[f]);
					else begin
						and (g[f], A[f], B[f]);
                                        	xor (p[f], A[f], B[f]);
						and (gp[f], p[f], gg[f-1]);
						or (gg[f], g[f], gp[f]);
					end					
				end
		endgenerate
      	assign GG=gg[i];		
endmodule
