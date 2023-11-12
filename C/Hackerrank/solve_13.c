//https://www.hackerrank.com/challenges/frequency-of-digits-1/problem?isFullScreen=true
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char stri[1000000]={'\0'};
    int fre[10]={0};
    scanf("%[^\n]",stri);
    for(int i =0; i<strlen(stri);i++){
        if(stri[i] >= '0' && stri[i] <= '9'){
            fre[stri[i] - '0']++;
        }
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", fre[i]);
    }  
    return 0;
}
/*
Sample Input 0

a11472o5t6
Sample Output 0

0 2 1 0 1 1 1 1 0 0 
*/