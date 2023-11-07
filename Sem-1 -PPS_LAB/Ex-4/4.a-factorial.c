#include <stdio.h>
int fact1(int);
int main()
{
    int fact,n;
    printf("Enter a number to find factorial: ");
    scanf("%d",&n);
    fact = fact1(n);
    printf("The factorial of %d is: %d",n,fact);
    return 0; 
}
int fact1(int n)
{
    int x, fact=1;
    for(x=1;x<=n; x++)
    fact=fact*x;
    return fact; 

}