//https://www.hackerrank.com/challenges/reverse-array-c/problem?isFullScreen=true
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
    /* Write the logic to reverse the array. */
    for(i = 0; i < num/2; i++){
        int temp = arr[i];
        arr[i] = arr[num-i-1];
        arr[num-i-1] = temp;
    }
    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    free(arr);
    return 0;
}
/*
Sample Input 1

7
1 13 15 20 12 13 2 
Sample Output 1

2 13 12 20 15 13 1 
Sample Input 2

8
15 5 16 15 17 11 5 11 
Sample Output 2

11 5 11 17 15 16 5 15 
*/