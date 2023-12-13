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

struct employees* pointer_em;

int main() {
    int no_employees = 0;

    printf("How many employees do you have: ");
    scanf("%d", &no_employees);
    pointer_em = (struct employees*)malloc(sizeof(struct employees) * no_employees);

    if (pointer_em == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < no_employees; i++) {
        printf("\nEnter the name of employee: ");
        scanf(" %30[^\n]", pointer_em[i].name);
        printf("Enter the age of %s: ", pointer_em[i].name);
        scanf(" %d", &pointer_em[i].age);
        printf("Enter the number of hours %s worked: ", pointer_em[i].name);
        scanf(" %f", &pointer_em[i].hrs_worked);
        printf("Enter the per hour pay for %s: ", pointer_em[i].name);
        scanf(" %f", &pointer_em[i].hrly_pay);
        printf("Enter the tax rate (%%) for %s: ", pointer_em[i].name);
        scanf(" %f", &pointer_em[i].tax);

        pointer_em[i].gross_pay = pointer_em[i].hrs_worked * pointer_em[i].hrly_pay;
        pointer_em[i].fin_tax = (pointer_em[i].tax / 100) * pointer_em[i].gross_pay;
        pointer_em[i].fin_amount = pointer_em[i].gross_pay - pointer_em[i].fin_tax;
    }

    for (int i = 0; i < no_employees; i++) {
        printf("\nEmployee %d: Name: %s\nAge: %d\nHours Worked: %.2f\nHourly Pay: %.2f\nGross Pay: %.2f\nTax(%%): %.2f\nTax Reduction: %.2f\nFinal Amount: %.2f\n",
            i + 1,
            pointer_em[i].name,
            pointer_em[i].age,
            pointer_em[i].hrs_worked,
            pointer_em[i].hrly_pay,
            pointer_em[i].gross_pay,
            pointer_em[i].tax,
            pointer_em[i].fin_tax,
            pointer_em[i].fin_amount
        );
    }

    free(pointer_em);
    return 0;
}
