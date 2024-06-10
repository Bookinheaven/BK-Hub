module testbench;
    reg [1:0] S;
    reg [3:0] I;
    wire Y;
    Mux_4_1 mux_inst (
        .Y(Y),
        .S(S),
        .I(I)
    );
    initial begin
        $monitor("S = %b, I = %b, Y = %b", S, I, Y);
        
        // Test case 1
        S = 2'b00; // Select input: 00
        I = 4'b0001; // Input data: 0001
        #10; // Wait for 10 time units
        // Expected output: 0001, as S selects I[0]
        
        // Test case 2
        S = 2'b01; // Select input: 01
        I = 4'b0110; // Input data: 0110
        #10; // Wait for 10 time units
        // Expected output: 0110, as S selects I[1]
        
        // Test case 3
        S = 2'b10; // Select input: 10
        I = 4'b1010; // Input data: 1010
        #10; // Wait for 10 time units
        // Expected output: 1010, as S selects I[2]
        
        // Test case 4
        S = 2'b11; // Select input: 11
        I = 4'b1100; // Input data: 1100
        #10; // Wait for 10 time units
        // Expected output: 1100, as S selects I[3]
        
        $finish;
    end

endmodule
