#include <stdio.h>

int main(){
    int num_in_ls;
    printf("Enter the elements in the list: ");
    scanf("%d",&num_in_ls);
    int input_list[num_in_ls],sum;
    int* pointer = input_list;
    printf("Enter the numbers in the elements\n");
    for(int x=1; x<= num_in_ls; x++){
        printf(" %d ==> ",x);
        scanf("%d", &input_list[x-1]); 
        sum += *(pointer++);
    }

    printf("%d",sum);
}
