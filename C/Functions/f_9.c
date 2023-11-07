
/*
C Program to Calculate Power Using Recursion
*/

#include <stdio.h>

int power(int num,int pow){//function declaration
    //function definition
    if(pow !=0){
        return num * power(num, pow-1);
    }
    return 1;
}
int main(){
    int num =0,pow=0,result=0;
    printf("Enter the number and power: ");
    scanf(" %d %d",&num,&pow);
    if(num<0){
        return printf("Can't find it");
        
    }
    result = power(num, pow);// function call---> num and pow is arguments
    printf("Power of \"%d\": %d",num,result);
    return 0;


}