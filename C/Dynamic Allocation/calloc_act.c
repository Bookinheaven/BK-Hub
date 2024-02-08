#include <stdio.h>
#include <stdlib.h>
int main() {
    int n = 5;
    int* ptr= (int*)calloc(n, sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed.\n");
        return -1;
    }
    for (int i = 0; i < n; ++i) {
        printf("%d ", ptr[i]); // Output: 0 0 0 0 0
    }
    free(ptr);
    return 0;
    
}
