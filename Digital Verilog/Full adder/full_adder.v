/*Data Flow:
module full_adder(x,y,cin,sum,cout);
  input x,y,cin;
  output sum,cout;
  assign sum = x^y^cin;
  assign cout = ((x&y)|(y&cin)|(x&cin));
endmodule
*/
/*Gate Level */
//Method #1
module full_adder(x,y,cin,sum,cout);
  input x, y, cin;
  output sum, cout;

  wire x_xor_y;
  xor(x_xor_y, x,y);
  xor(sum,x_xor_y,cin);
  
  wire y_and_x;
  and(y_and_x,y,x);
  
  wire cin_and_x_xor_y;
  and(cin_and_x_xor_y, x_xor_y,cin);
  
  or(cout, y_and_x,cin_and_x_xor_y);
/*
//Method 2
  wire x_xor_y;
  wire x_and_y;
  wire y_and_cin;
  wire x_and_cin;
  wire carry_intermediate;

  assign x_xor_y = x ^ y;
  assign sum = x_xor_y ^ cin;

  assign x_and_y = x & y;
  assign y_and_cin = y & cin;
  assign x_and_cin = x & cin;

  assign carry_intermediate = x_and_y | y_and_cin | x_and_cin; 

  assign cout = carry_intermediate;
*/
endmodule
  
