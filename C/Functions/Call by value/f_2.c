/*
C Program to Display Prime Numbers Between Two Intervals Using Functions 
*/
#include <stdio.h>

int dis_prime(int num);//function declaration

int main(){   
    int num_1 = 0,num_2=0;
    printf("Enter numbers to check its prime or not!: ");
    scanf("%d %d",&num_1,&num_2);
    printf("Prime Numbers from %d to %d are :\n",num_1,num_2);
    for(int num = 0; num<=num_2; num++){
        dis_prime(num);// function call---> num is arguments
    }
    return 0;
}
int dis_prime(int num){
    if(num ==0||num ==1){//function definition
        printf("%d\n",num);
        return 0;
    }
    for(int i=2; i<=num/2; i++){
        if ((int)num%i ==0) {
            return 0;
        }
    }
    printf("%d\n",num);
    return 0;
}