#include <stdio.h>
#include <stdlib.h>

int main() {
    int size = 5;
    int *dynamicArray = (int *)malloc(size * sizeof(int));

    if (dynamicArray == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < size; i++) {
        dynamicArray[i] = i;
        /*
        In C, arrays and pointers are closely related. 
        When you allocate memory for an array dynamically using malloc, 
        the name of the array is treated as a pointer to the first element of the array. 
        Therefore, when you write dynamicArray[i], iSt is equivalent to *(dynamicArray + i).

        Here, dynamicArray is a pointer to the first element of the dynamically allocated array.
        So, both of the following expressions are valid and equivalent:

        dynamicArray[i] = i;        // Using array syntax
        *(dynamicArray + i) = i;    // Using pointer arithmetic
        Both statements achieve the same result of assigning the value of i to the i-th element of the dynamically allocated array.
        */
    }

    for (int i = 0; i < size; i++) {
        printf("%d ", dynamicArray[i]);
    }

    free(dynamicArray);

    return 0;
}

