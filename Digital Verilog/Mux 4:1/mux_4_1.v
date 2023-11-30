module Mux_4_1(Y,S,I);
  input [1:0] S;
  input [3:0] I;
  output Y;
  assign Y = (~S[0] & ~S[1] & I[0]) | (S[0] & ~S[1] & I[1]) | (~S[0] & S[1] & I[2]) | (S[0] & S[1] & I[3]);
  
endmodule
