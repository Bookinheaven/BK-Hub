#include <stdio.h>

int main(){
    
    int arr[] = {5,3,2,7,1,9,4};
    int n =sizeof(arr)/sizeof(arr[0])-1;
    printf("Before Array: [ ");
    for(int i =0; i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("]\n");
    
    for(int i =0; i<n; i++){
        int min_term = i;
        for(int j = i+1; j<n;j++){
            if(arr[j] < arr[min_term]){
                min_term = j;
            }
        }
        int temp = arr[min_term];
        arr[min_term] = arr[i];
        arr[i] = temp;
    }

    printf("After Array:  [ ");
    for(int i =0; i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("]");
    return 0;
}