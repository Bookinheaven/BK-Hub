
module full_adder(x,y,cin,sum,cout);
  input x,y,cin;
  output sum,cout;
  assign sum = x^y^cin;
  assign cout = ((x&y)|(y&cin)|(x&cin));
endmodule