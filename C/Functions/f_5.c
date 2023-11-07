
/*
C Program to Find the Sum of Natural Numbers using Recursion 
*/
#include <stdio.h>

int natural_num(int num){//function declaration
    if(num ==0){//function definition
        return 0;
    }
    return num + natural_num(num-1);
}
int main(){
    int num =0,result=0;
    printf("Enter the number: ");
    scanf(" %d",&num);
    if(num<0){
        return printf("Natural Numbers are from 1");
        
    }
    result = natural_num(num);// function call---> num is argument
    printf("Sum of first \"%d\" Numbers: %d",num,result);
    return 0;


}