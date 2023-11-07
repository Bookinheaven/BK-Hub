#include <stdio.h>


int main(){
    int a,b,temp;
    printf("Enter two numbers a and b ");
    scanf("%d%d",&a,&b);
    printf("\nBefore Swapping \na=%d b=%d\n",a,b);
    temp = a;
    a=b;
    b=temp;
    printf("\nAfter Swapping \na=%d b=%d",a,b);
    return 0;
}
