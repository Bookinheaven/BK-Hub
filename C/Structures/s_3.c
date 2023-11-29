#include <stdio.h>
#include <stdlib.h>
struct vehicles {
    long int registration_number;
    char model_name[20];
};
int main(){
    
    struct vehicles *ptr;
    int n = 3;
    ptr = (struct vehicles *) calloc(n,sizeof(*ptr));
    if(ptr == NULL){
        printf("Not Allocated");
        return 1;
    }
    printf("Enter the details vehicles :\n");
    for(int i = 0; i<n; i++){
        printf("Vehicle (%d) reg.no: ",i+1);
        scanf("%ld", &ptr[i].registration_number);
        printf("Vehicle (%d) model name: ",i+1);
        getchar();
        scanf("%19[^\n]", ptr[i].model_name);
    }
    for(int i = 0; i<n; i++){
        printf("\nVehicle (%d) reg.no: %ld ",i+1, ptr[i].registration_number);
        printf("\nVehicle (%d) model name %s: ",i+1, ptr[i].model_name);
    }
    free(ptr);


}