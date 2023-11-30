/*Data Flow:
module half_adder(input a,b,
                  output s,c);
  assign s = a^b;
  assign c = a&b;
  
endmodule
*/
/*Gate Level:*/
//Method #1
module half_adder(input a,b,
                  output s,c);
  /*
  wire a_b_xor;
  wire a_b_and;

  assign a_b_xor = a ^ b;
  assign a_b_and = a & b;
  assign s = a_b_xor;
  assign c = a_b_and;
  */
//Method #2
  
  xor(s, a,b);
  and(c,a,b);
  
  
endmodule