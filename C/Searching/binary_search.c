#include <stdio.h>

int main(){
    int arr[] = {1,3,5,7,9,10,12,13,16,18},n = sizeof(arr)/sizeof(arr[0])-1, low = 0, high = n,search = 16;
    while(low<=high){
        int mid = (high-low)/2 + low ;
        if(arr[mid] == search){
            printf("Found %d element",mid+1);
            break;
        }
        else if(arr[mid] < search){
            low = mid+1;
        }
        else{
            high = mid -1;
        }
    }
    return 0;
}