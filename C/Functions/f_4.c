
/*
C Program to Check Whether a Number can be Express as Sum of Two Prime Numbers
*/
#include <stdio.h>
#include <stdbool.h>
bool check_prime(int num);//function declaration

int main(){   
    int num=0;
    printf("Enter number to check its prime or not!: ");
    scanf("%d",&num);
    for(int i = 2; i<num/2; i++){
        if (check_prime(i) && check_prime(num - i)) {// function call---> num and i is arguments
            printf("%d + %d = %d\n", i, num - i, num);
        }
        else {
            printf("We Can't do it!!");
        }
    }
    return 0;
}
bool check_prime(int num){
    if(num ==0||num ==1){//function definition
        printf("%d\n",num);
        return false;
    }
    else {
    for(int i=2; i<=num/2; i++){
        if ((int)num%i ==0) {
            return false;
        }
    }
    return true;
    }
}