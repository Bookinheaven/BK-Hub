#include <stdio.h>

int function_largest(int[],int);


int main() {
   int input_num;
    printf("How many elements are present in the list: ");
    scanf("%d",&input_num);
   
    printf("\nWhat are the elements in the list?\n ");
    int input_list[input_num];
    for(int x=1; x<= input_num; x++){
        printf("\n%d ==> ",x);
        scanf("%d", &input_list[x-1]);
       
    }
    
    function_largest(input_list,input_num);

    return 0;
}

int function_largest(int input_list[], int input_num){
    int largest_number = input_list[0] ;
    for(int y=0; y<=input_num;y++){
        if(input_list[y] > largest_number){
            largest_number = input_list[y];
        }
    }
    printf("%d", largest_number);
    return 0;
}
