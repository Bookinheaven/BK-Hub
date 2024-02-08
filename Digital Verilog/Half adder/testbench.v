module test;
  reg a, b;
  wire s, c;
  integer i;
  
  half_adder DUT(a,b,s,c);
  
  initial
    begin
      for(i=0;i<4;i =i+1)
        begin 
          #5;
          {a,b} = i;
          $monitor("input a = %b b = %b \noutput sum = %b, carry = %b",a,b,s,c);
    	end
    	end
               
endmodule
               
         