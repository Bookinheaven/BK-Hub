#include <stdio.h>

int main(){
    
    int arr[] = {5,3,2,7,1,9,4};
    int n =sizeof(arr)/sizeof(arr[0])-1;
    printf("Before Array: [ ");
    for(int i =0; i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("]\n");
    for(int i = 0; i<n;i++){
        for(int j = 0; j<n-i; j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }

    }
    printf("After Array:  [ ");
    for(int i =0; i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("]");
    return 0;
}