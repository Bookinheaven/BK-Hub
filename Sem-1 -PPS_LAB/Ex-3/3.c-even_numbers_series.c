#include <stdio.h>

int main() {
    int i,n,sum=0;
    printf("Input number of terms: ");
    scanf("%d",&n);
    printf("The even numbers are: ");
    for(i=1;i<=n;i++){
        printf("%d ",2*i);
        sum+= 2*i;
    }
    printf("\nThe Sum even numbers upto %d terms: %d\n",n,sum);

    return 0;
}