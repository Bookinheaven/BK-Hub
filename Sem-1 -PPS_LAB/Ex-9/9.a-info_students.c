#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
struct employees {
    char name[10];
    int age;
    float hrs_worked;
    float hrly_pay;
    float tax;
    float gross_pay;
    float fin_tax;
    double fin_amount;
    };
struct employees* ponter_em;
int main() {
    int no_employees=0;
    printf("How many employees you have: ");
    scanf("%d",&no_employees);
    ponter_em = (struct employees*) malloc(sizeof(struct employees)*no_employees);

    if (ponter_em == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }
    for (int i = 0; i < no_employees; i++) {
        ponter_em[i].name[0] = '\0'; 
        ponter_em[i].age = 0;
        ponter_em[i].hrs_worked = 0.0;
        ponter_em[i].hrly_pay = 0.0;
        ponter_em[i].tax = 0.0;
        ponter_em[i].gross_pay = 0.0;
        ponter_em[i].fin_tax = 0.0;
        ponter_em[i].fin_amount = 0.0;
    }
    for (int i=0; i<no_employees; i++){
        printf("\nEnter the name of employee: ");
        scanf(" %30[^\n]", ponter_em[i].name);
        printf("Enter the age of %s: ", ponter_em[i].name);
        scanf(" %d", &ponter_em[i].age);
        printf("Enter the number of hours %s worked: ", ponter_em[i].name);
        scanf(" %f", &ponter_em[i].hrs_worked);
        printf("Enter the per hour %s pay: ", ponter_em[i].name);
        scanf(" %f", &ponter_em[i].hrly_pay);
        printf("Enter the tax (%%): ");
        scanf(" %f", &ponter_em[i].tax);
        ponter_em[i].gross_pay = ponter_em[i].hrs_worked * ponter_em[i].hrly_pay;
        ponter_em[i].fin_tax = (ponter_em[i].tax / 100) * ponter_em[i].gross_pay;
        ponter_em[i].fin_amount = ponter_em[i].gross_pay - ponter_em[i].fin_tax;
    }
    for (int i = 0; i < no_employees; i++) {
        printf("\nEmployee %d: Name: %s\nAge: %d\nHours Worked: %.2f\nHours Pay: %.2f\nGross Pay: %.2f\nTax(%%): %.2f\nTax Reduction: %.2f\nFinal Amount: %.2f\n", 
        i + 1,
        ponter_em[i].name,
        ponter_em[i].age,
        ponter_em[i].hrs_worked,
        ponter_em[i].hrly_pay,
        ponter_em[i].gross_pay,
        ponter_em[i].tax,
        ponter_em[i].fin_tax,
        ponter_em[i].fin_amount
        );
    }
    free(ponter_em);

    return 0;
}
