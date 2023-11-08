/*
C Program to Check Whether a Number is Prime or Not
*/

#include <stdio.h>

int main(){
    double num=0, stop=0;
    printf("Enter the numbers: ");
    scanf("%lf",&num);
    if(num<= 1){
        printf("Its Not prime number");
    }
    for(int i=2; i<=num; i++){
        if((int)num %i ==0){
            stop =1;
            break;
            
        }
    }
    if(stop == 0){
        printf("Its Not prime number");
    }
    else{
        printf("Its prime number");
    }
    return 0;

}