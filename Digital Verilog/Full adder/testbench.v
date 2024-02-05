module testbench;
  reg x,y,cin;
  wire sum,cout;
  full_adder DUT (x,y,cin,sum,cout);
  initial begin
    $dumpfile("test.vcd");
    $dumpvars(1);
    x=0;
    y=0;
    cin=0;
    #200 $finish;
  end
  always #3 x=~x;
  always #5 y=~y;
  always #7 cin=~cin;
endmodule