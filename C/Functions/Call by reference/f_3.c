#include <stdio.h>

void ca_pointer(int *ptr,int size){
    for(int i =0; i<size; i++){
        *(ptr+i) +=5;
    }
}

int main(){
    int arr[] = {1,2,3,4,5,6,7,8};
    int *ptr = arr;
    int size = sizeof(arr)/ sizeof(arr[0]);
    ca_pointer(ptr,size);

    for(int i =0 ;i <size; i++){
        printf("%d ",arr[i]);
    }
    return 0;
    
}