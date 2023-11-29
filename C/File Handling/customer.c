#include <stdio.h>

int main() {
    FILE *data = fopen("../customer.txt","w");
    if(data == NULL) {
        perror("Data Not found");
    }
    char name[16];
    char address[21];
    int id = 0;
    int n = 2;
    unsigned long int contact_no =0;
    for(int i = 0; i < n; i++){
        printf("\nEnter the name: ");
        getchar();
        scanf("%15[^\n]",name);
        getchar();
        printf("Enter the address: ");
        scanf("%20[^\n]",address);
        printf("Enter the id: ");
        scanf("%d",&id);
        printf("Enter the contact no: ");
        scanf("%lu", &contact_no);

        fprintf(data, "Name: %s\n",name);
        fprintf(data, "Address: %s\n",address);
        fprintf(data, "ID: %d\n",id);
        fprintf(data, "Contact Number: %lu\n\n",contact_no);
    }

    fclose(data);
}