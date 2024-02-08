#include <stdio.h>

struct employees{
    char empName[50];
    int empID;
    char companyName[50];
    int yearsofExperience;
};

int main(){
    struct employees ep[3];

    for(int i =0; i< 3; i++){
        printf("\nEnter Details of ep %d\n",i+1);

        printf("Name: ");
        scanf("%s", ep[i].empName);
        
        printf("ID: ");
        scanf("%d", &ep[i].empID);

        printf("Company Name: ");
        scanf("%s", ep[i].companyName);

        printf("Years Of Experience: ");
        scanf("%d", &ep[i].yearsofExperience);
    }

    for(int i =0; i< 3; i++){
        printf("\Details of ep %d\n",i+1);
        printf("\nName %s: ",ep[i].empName);
        printf("\nID: %d", ep[i].empID);
        printf("\nCompany Name: %s", ep[i].companyName);
        printf("\nYears Of Experience: %d",ep[i].yearsofExperience);
    }

}