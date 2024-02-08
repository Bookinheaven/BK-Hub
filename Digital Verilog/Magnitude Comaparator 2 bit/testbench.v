module magnitude_comparator_tb;
    reg [1:0] A, B;
    wire a_less_b, a_greater_b, a_equal_b;
	integer i, j;
    magnitude_comparator_2_bits comparator_inst (
        .A(A),
        .B(B),
        .a_less_b(a_less_b),
        .a_greater_b(a_greater_b),
        .a_equal_b(a_equal_b)
    );

    initial begin
        $monitor("A = %b, B = %b, A < B = %b, A > B = %b, A = B = %b", A, B, a_less_b, a_greater_b, a_equal_b);

        for (i = 0; i < 4; i = i + 1) begin
            for (j = 0; j < 4; j = j + 1) begin
                A = i;
                B = j;
                #5; 
                $display("A = %b, B = %b, A < B = %b, A > B = %b, A = B = %b", A, B, a_less_b, a_greater_b, a_equal_b);
            end
        end
        $finish;
    end

endmodule
