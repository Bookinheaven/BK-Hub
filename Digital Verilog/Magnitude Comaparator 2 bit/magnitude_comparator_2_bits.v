
module magnitude_comparator_2_bits(A,B,a_less_b,a_greater_b,a_equal_b);
  input [1:0] A;
  input [1:0] B;
  output a_less_b, a_greater_b,a_equal_b;
  assign a_less_b = (~A[1] & B[1]) | (~A[1] &~A[0] & B[0]) | (~A[0] & B[1] & B[0]);
  assign a_greater_b = (A[1] & ~B[1]) | (A[0] & ~B[1] & ~B[0]) | (A[1] & A[0] & ~B[0]);
  assign a_equal_b = (~(A[1] ^ B[1])) & (~(A[0] ~^ B[0]));
  
endmodule