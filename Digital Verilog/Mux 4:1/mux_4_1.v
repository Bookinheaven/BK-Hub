module Mux_4_1(Y,S,I);
  input [1:0] S;
  input [3:0] I;
  output Y;
  /*Data Flow:
  assign Y = (~S[0] & ~S[1] & I[0]) | (S[0] & ~S[1] & I[1]) | (~S[0] & S[1] & I[2]) | (S[0] & S[1] & I[3]);
  */
  /*Gate Level:*/
  //Method #1
  wire not_S0, not_S1;
  wire and_gate0, and_gate1, and_gate2, and_gate3;
  wire or_gate0, or_gate1, or_gate2;

  assign not_S0 = ~S[0];
  assign not_S1 = ~S[1];

  assign and_gate0 = I[0] & not_S0 & not_S1;
  assign and_gate1 = I[1] & S[0] & not_S1;
  assign and_gate2 = I[2] & not_S0 & S[1];
  assign and_gate3 = I[3] & S[0] & S[1];

  assign or_gate0 = and_gate0 | and_gate1;
  assign or_gate1 = and_gate2 | and_gate3;

  assign Y = or_gate0 | or_gate1; 
  
  
endmodule