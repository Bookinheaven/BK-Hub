#include <stdio.h>
#include <stdlib.h>
int main(){
    int num = 5,i=0;
    int *ptr = (int *)malloc(num* sizeof(int));
    if(ptr == NULL){
        perror("NOT ALLOCATED");
    }
    for(;i<num;){
        i++;
        ptr[i] = i+1;
    }
    printf("Values Allocated!\n");
    for(i=0;i<num;){
        i++;
        printf("Allocated data (%d)--> %d \n",i,ptr[i]);
    }
    free(ptr);
    return 0;
}
