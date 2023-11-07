/*
C Program for finding fibonacci series between two numbers
*/
/*
 1 + 1 = 2
 1 + 2 = 3
 2 + 3 = 5
 .........

*/
#include <stdio.h>

int fibonacci(int n) {//function declaration
    //function definition
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int num_1, num_2;
    
    printf("Enter two numbers to check Fibonacci numbers between them: ");
    scanf("%d %d", &num_1, &num_2);

    if (num_1 <= 0 || num_2 <= 0 || num_1 > num_2) {
        printf("Cant Find it.");
    } else {
        for (int i = 1; fibonacci(i) <= num_2; i++) {//function call --> i argument 
            int fib = fibonacci(i);
            if (fib >= num_1) {
                printf("%d ", fib);
            }
        }
        printf("\n");
    }

    return 0;
}
