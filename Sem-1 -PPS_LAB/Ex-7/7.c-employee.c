#include <stdio.h>

float gross_pay(float hrs_worked, float hrly_pay) {
    return hrs_worked * hrly_pay;
}
float tax(float gross_pay, float in_tax) {
    return (in_tax/100) * gross_pay;
}
int main() {
    float hrs_worked, hrly_pay, fin_gross_pays, fin_taxs, fin_amount,in_tax;
    printf("Enter hours you worked: ");
    scanf("%f", &hrs_worked);
    printf("Enter hourly how much you earn: ");
    scanf("%f", &hrly_pay);
    printf("Enter tax percentage(1.00-100.00): ");
    scanf("%f", &in_tax);
    fin_gross_pays = gross_pay(hrs_worked, hrly_pay);
    fin_taxs = tax(fin_gross_pays,in_tax);
    fin_amount = fin_gross_pays - fin_taxs;
    printf("Gross Pay: ₹%.2f\n", fin_gross_pays);
    printf("Tax Deduction: ₹%.2f\n", fin_taxs);
    printf("Net worth: ₹%.2f\n", fin_amount);
    return 0;
}
