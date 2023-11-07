/*
C Program to Calculate the Factorial of a Number Using Recursion 
*/

#include <stdio.h>

int factorial(int num){//function declaration
    if(num ==0){//function definition
        return 1;
    }
    return num * factorial(num-1);
}
int main(){
    int num =0,result=0;
    printf("Enter the number: ");
    scanf(" %d",&num);
    if(num<0){
        return printf("Can't Find for negetive numbers");
        
    }
    result = factorial(num);// function call---> num is argument
    printf("Factorial of \"%d!\": %d",num,result);
    return 0;


}
