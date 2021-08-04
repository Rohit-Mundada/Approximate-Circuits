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
module BIT_P(output BP, input A, B);

   xor (BP, A, B);

endmodule
