#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Enter two numbers a and b: ");
    scanf("%d %d",&a,&b);
    c = (a+b)*(a+b);
    printf("\nSquare of a=%d b=%d is %d\n",a,b,c);
    return 0;
}
