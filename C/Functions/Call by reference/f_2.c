#include <stdio.h>
void fun(int *num, size_t n){
    for(size_t i =0; i<n;i++){
        *(num+i) = i + 1; 
    }
}
int main(){
    int num[] = {6,7,8,3,21,1};
    size_t n = sizeof(num)/sizeof(num[0]);
    printf("Before [ ");
    for(size_t i = 0; i < n; i++){
        printf("%d ",num[i]);
    }
    printf("]\n");
    fun(num, n);
    printf("After [ ");
    for(size_t i = 0; i < n; i++){
        printf("%d ",num[i]);
    }
    printf("]\n");
}