/*
C Program to Print an Integer Entered By the User
*/

#include <stdio.h>

int main(){
    int num_1=0,num_2=0;
    printf("Enter two numbers: ");
    scanf("%d %d",&num_1,&num_2);
    printf("Num-1: %d\nNum-2: %d", num_1,num_2);
    return 0;
}