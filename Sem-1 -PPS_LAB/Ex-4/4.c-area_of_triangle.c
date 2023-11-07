#include <stdio.h>
void area_of_triangle(double, double);
int main()
{
    double a,b;
    printf("Enter the first number: ");
    scanf("%lf", &a);
    printf("Enter the second number: ");
    scanf("%lf", &b);
    area_of_triangle(a,b);
    return 0;
}
void area_of_triangle(double a, double b){
    double areaoftriangle = 0.5*a*b;
    printf("\nArea of triangle: %.2lf", areaoftriangle);
}