#include <stdio.h>

int main() {
    float unit, amount, s_change, total_amount;
    printf("Enter Value: ");
    scanf("%f", &unit);
    if(unit <=50) {
        amount = unit*0.05;
        s_change = amount*0.20;
    }
    else if (unit <=150)
    {
        amount = 25+(unit-50)*0.75;
        s_change = amount*0.20;
    }  
    else if (unit <=250)
    {
        amount = 100+(unit-150)*1.20;
        s_change = amount*0.20;
    }
    else {
        amount = 220+(unit-250)*1.50;
    }
    total_amount = amount+s_change;
    printf("Total Amount: %f", total_amount);
    
    return 0;
}