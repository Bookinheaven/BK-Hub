/*
C Program to Swap Two Numbers
*/

#include <stdio.h>
int main(){
    int a,b,temp;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("Before Swapping \n1= %d 2= %d",a,b);
    temp = a;
    a=b;
    b=temp;
    printf("\nAfter Swapping \n1= %d 2= %d",a,b);
    return 0;
}
