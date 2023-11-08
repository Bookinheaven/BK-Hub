
/*
C Program to Multiply two Floating-Point Numbers 
*/
#include <stdio.h>

int main(){
    float num_1=0.0,num_2=0.0;
    printf("Enter two numbers: ");
    scanf("%f %f",&num_1,&num_2);
    printf("Product = %.3f", num_1*num_2);
    return 0;
}