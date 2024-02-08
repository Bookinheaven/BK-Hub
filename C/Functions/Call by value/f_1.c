/*
C Program to Check Prime Number By Creating a Function 
*/

#include <stdio.h>

int check_prime(int num);//function declaration

int main(){
    int num = 0;
    printf("Enter number to check its prime or not!: ");
    scanf("%d",&num);

    int y = check_prime(num);// function call---> num is arguments
    if(y==1){
        printf("Its not a prime number!");
    }
    else{
        printf("Its a prime number!");
    }
    return 0;
}
int check_prime(int temp) {//function definition
    if(temp ==0||temp ==1){
        return 1;
    }
    for(int i=2; i<=temp/2; i++){
        if ((int)temp%i ==0) {
            return 1;
        }
    }
    return 0;
}
