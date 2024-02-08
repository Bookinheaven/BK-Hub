#include <stdio.h>

int main(){
    int arr[] = {10,12,43,13,11,65,32};
    int n = sizeof(arr)/ sizeof(arr[0]);
    int search = 65;
    for(int i = 0; i<n;i++){
        if(arr[i] == search){
            printf("Found it %d element", i+1);
        }
    }
    return 0;
}