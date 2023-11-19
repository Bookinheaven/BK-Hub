module testbench;

  reg [7:0] I;
  reg [2:0] S;
  wire Y_output; 
  integer i, j;
  MUX_1_8 DUT ( I,S,Y_output);
  
  initial begin
    $dumpfile("muxtest.vcd");
    $dumpvars(0, testbench);
    for (i = 0; i < 8; i = i + 1) begin
      S = i;
      
      for (j = 0; j < 256; j = j + 1) begin
        I = j;
        #10; 
        
        $display("Input: I = %b, S = %b, Output Y = %b", I, S, Y_output);
      end
    end
    
    $finish;
  end
  
endmodule
