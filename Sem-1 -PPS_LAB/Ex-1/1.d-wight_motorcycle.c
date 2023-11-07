#include <stdio.h>

int main() {
    float weight_1st_wheel, weight_2nd_wheel, total_weight;
    printf("Enter Weight Of First Wheel(kg or pounds): ");
    scanf("%f", &weight_1st_wheel);
    printf("\nEnter Weight Of Second Wheel(kg or pounds): ");
    scanf("%f", &weight_2nd_wheel);
    total_weight = weight_1st_wheel+weight_2nd_wheel;
    printf("Total Weight of Motor Cycle is %f", total_weight);
    return 0;
}