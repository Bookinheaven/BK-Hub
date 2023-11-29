#include <stdio.h>

int rec(int *ptr,int size){
    int sum = 0;
    if(size == 0){
        return sum;
    } 
    else{
        sum += *ptr;
        return sum + rec(ptr+1, size-1);
    }
}

int main(){
    int arr[]= {1,2,3,4,5,6};
    int size = sizeof(arr)/sizeof(arr[0]);
    int sum = rec(arr, size);
    printf("Sum : %d", sum);
    return 0;   
}