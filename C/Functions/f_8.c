/*
C Program to Reverse a Stack using Recursion
*/

#include <stdio.h>

void reverse(int num[], int start, int end) {//function declaration
    //function definition
    if (start >= end) {
        return;
    }

    int temp = num[start];
    num[start] = num[end];
    num[end] = temp;

    reverse(num, start + 1, end - 1);
}

int main() {
    int num[5] = {0};

    printf("Enter five numbers: ");
    scanf("%d %d %d %d %d", &num[0], &num[1], &num[2], &num[3], &num[4]);

    printf("Original Array: [");
    for (int i = 0; i < 5; i++) {
        printf("%d ", num[i]);
    }
    printf("]\n");

    reverse(num, 0, 4);// function call---> num,0, 4 is arguments

    printf("Reversed Array: [");
    for (int i = 0; i < 5; i++) {
        printf("%d ", num[i]);
    }
    printf("]\n");

    return 0;
}