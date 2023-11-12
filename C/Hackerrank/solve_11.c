//https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=true
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, *arr; 
    scanf("%d", &n);
    arr = (int *) malloc(n*sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    for (int i = 0; i < n; i++)
        scanf("%d", arr+i);
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += *(arr+i);
    printf("%d", sum);
    free(arr);
    return 0;
}
/*
Sample Input 0

6
16 13 7 2 1 12 
Sample Output 0

51
Sample Input 1

7
1 13 15 20 12 13 2 
Sample Output 1

76
*/