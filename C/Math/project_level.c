#include <stdio.h>
#include <math.h>
#define PI 3.14

void matrix_dis(int matrix[3][3],int z){// z=0 display
    
    for (int i = 0; i < 3; i++) {
        if(z==0) printf("|");
        for (int j = 0; j < 3; j++) {
            if(z==0){
                printf("%3d", matrix[i][j]);
            }
            else{
                printf("( %dx%d ): ", i+1, j+1);
                if (scanf("%3d", &matrix[i][j]) != 1) {
                    printf("Invalid input.\n");
                    return;
                }
            }
        }
        if(z ==0) printf("|\n");
    }
}

int matrix_det(int matrix[3][3]) {
    int det = 0;

    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
          matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
          matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    return det;
}

void find_roots(int matrix[3][3]){
    // ax^3-bx^2+cx-d =0
    // a = -sum of the diagonal elements 
    // b = sum of the minors of the diagonal element
    // c = -det
    int det = matrix_det(matrix);
    int a = 1;
    int b = - (matrix[0][0] + matrix[1][1] + matrix[2][2]);
    int c = matrix[0][0] * matrix[1][1] + matrix[1][1] * matrix[2][2] + matrix[2][2] * matrix[0][0] -
            matrix[0][1] * matrix[1][0] - matrix[1][2] * matrix[2][1] - matrix[0][2] * matrix[2][0];
    int d = -det;
    /* 
    Cardano's formula to solve cubic equation: a * x^3 + b * x^2 + c * x + d = 0
    p = 3ac-b^2/3a^2 
    q = 2b^3-9abc+27a^2d
    Disc = q^2 + (p/3)^3
    
    u =  root 3 (-q/2+root 2(Disc))
    v =  root 3 (-q/2-root 2(Disc))
    */
    int p = c / a - (b * b) / (3 * a * a);
    int q = (2 * b * b * b) / (27 * a * a * a) - (b * c) / (3 * a * a) + d / a;
    double discriminant = (q * q) / 4 + (p * p * p) / 27;
    double eigenvalues[3];
    if (discriminant > 0) {
        double u = cbrt(-q / 2 + sqrt(discriminant)); 
        double v = cbrt(-q / 2 - sqrt(discriminant));
        eigenvalues[0] = u + v - b / (3 * a);
        printf("Eigenvalue 1: %.2lf\n", eigenvalues[0]);
    } else if (discriminant == 0) {
        double u = cbrt(-q / 2);
        eigenvalues[0] = 2 * u - b / (3 * a);
        eigenvalues[1] = -u - b / (3 * a);
        printf("Eigenvalue 1: %.2lf\n", eigenvalues[0]);
        printf("Eigenvalue 2: %.2lf\n", eigenvalues[1]);
    } else {
        double rho = sqrt((-p * p * p) / 27);
        double theta = acos(-q / (2 * rho));
        double u = cbrt(rho);
        eigenvalues[0] = 2 * u * cos(theta / 3) - b / (3 * a);
        eigenvalues[1] = 2 * u * cos((theta + 2 * PI) / 3) - b / (3 * a);
        eigenvalues[2] = 2 * u * cos((theta + 4 * PI) / 3) - b / (3 * a);
        printf("Eigenvalue 1: %.2lf\n", eigenvalues[0]);
        printf("Eigenvalue 2: %.2lf\n", eigenvalues[1]);
        printf("Eigenvalue 3: %.2lf\n", eigenvalues[2]);
    }
}

int main() {
    int matrix[3][3] = {{0}};
    printf("\t\t%10s\t \n","MatBKix");
    printf("Enter the values to find the characteristic eq (3x3): \n");
    matrix_dis(matrix,1);
    printf("Entered matrix: \n");
    matrix_dis(matrix,0);
    printf("Roots:\n");
    find_roots(matrix);
    
    return 0;
}
