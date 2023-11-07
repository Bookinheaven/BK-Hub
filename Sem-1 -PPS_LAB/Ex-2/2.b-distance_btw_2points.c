#include <stdio.h>
#include <math.h>

int main() {
    float x_1, y_1, x_2, y_2, distance, fin_x, fin_y;
    printf("Enter Point-1 (x1 y1): ");
    scanf("%f %f", &x_1, &y_1);
    printf("Enter Point-2 (x2 y2): ");
    scanf("%f %f", &x_2, &y_2);
    fin_x = x_2 - x_1;
    fin_y = y_2 - y_1;
    distance = sqrt((fin_x * fin_x) + (fin_y * fin_y));
    printf("Distance = %f\n", distance);
    return 0;
}
//gcc -o nameanything program.c -lm
//gcc -o d_c 2-b.c -lm
//cc filename -lm