//https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem?isFullScreen=true

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int n,next,sum;
    scanf("%d", &n);
    next = n;
    for(int i =0; i<5;i++){
        sum+= next%10;
        next = next/10;
    }
    printf("%d",sum);
    return 0;
}
/*
Sample Input 0

10564
Sample Output 0

16
*/