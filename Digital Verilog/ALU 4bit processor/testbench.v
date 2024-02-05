module testbench;

  reg [3:0] A, B;
  reg [2:0] s;
  wire [3:0] Y;
  integer i, j;

  alu_4_bit DUT (A, B, s, Y);

  initial begin 
    $dumpfile("test.vcd");
    $dumpvars(0, testbench);
    //s = 3'b000;
    for (i = 0; i < 4; i = i + 1) begin
      for (j = 0; j < 4; j = j + 1) begin
        A = i;
        B = j;
        s = 3'b000;/*sir we can change it depending on what operation we want to do. 
        I don't like to make the output mess up by using looping in operations too.
        */
        #10;
        $display("A=%d, B=%d, Result: %b", A, B, Y);
      end
    end
    
    #20;
    $finish;
  end

endmodule
