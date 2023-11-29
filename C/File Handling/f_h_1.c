#include <stdio.h>

int main(){
    FILE *data_pointer;
    char data[1000] = "\0";
    data_pointer = fopen("../test.txt","a+");
    if(data_pointer == NULL){
        perror("Cant find the file");
        return 1;
    }
/* 
    fgets(data,1000, data_pointer);
    printf("Data from file: \n%s\n",data);

    for(int i = 0; i < 10 ; i++) {
        fscanf(data_pointer,"%d",&data);
        printf("%d\n",data);
    }
*/
    while (fgets(data, sizeof(data), data_pointer) != NULL) {
        printf("%s", data); // Print each line of the file
    }
    
    fclose(data_pointer);
    return 0;
}