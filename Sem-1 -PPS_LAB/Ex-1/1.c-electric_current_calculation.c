#include <stdio.h>


int main() {
    float voltage, resistance, current, power_factor, electric_current;
    printf("\n Enter Voltage : ");
    scanf("%f",&voltage);
    printf("\n Enter Resistance: ");
    scanf("%f", &resistance);
    printf("\n Enter Current: ");
    scanf("%f", &current);
    printf("\n Enter Power Factor: ");
    scanf("%f", &power_factor);
    electric_current = 3*(voltage*resistance*current*power_factor);
    printf("%f", electric_current);
    return 0;
}