`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:        Pravin Mane
// 
// Create Date:    10:15:56 11/01/2019 
// Design Name: 
// Module Name:    Group propagate signal 
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

module group_p #(parameter i=1, j=0)(
	output GP, 
	input [i:j] A, B);

	wire [i:j] p;
	wire [i:j] gp;   

        genvar f;

		generate
			for(f=j; f<i+1; f=f+1)
				begin
					if (f==0)
						assign gp[f]=0;
					else if (f==j | f==1)
						xor (gp[f], A[f], B[f]);
					else begin
						xor (p[f], A[f], B[f]);
						and (gp[f], p[f], gp[f-1]);
					end					
				end
		endgenerate
      	assign GP=gp[i];		
endmodule
