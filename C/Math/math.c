#include <stdio.h>
#include <math.h>
#define PI 3.14

void matrix_dis(int matrix[3][3], int z, int k) {
    if (z == 3) {
        printf("Entered matrix: \n");
    }
    if (z == 1 && k) {
        printf("\nMatrix %d:\n", k);
    }
    for (int i = 0; i < 3; i++) {
        if (z == 0 || z == 3) {
            printf("|");
        }
        for (int j = 0; j < 3; j++) {
            if (z == 0 || z == 3) {
                printf("%5d", matrix[i][j]);
            } else if (z == 1) {
                printf("( %dx%d ): ", i + 1, j + 1);
                if (scanf("%d", &matrix[i][j]) != 1) {
                    printf("Invalid input.\n");
                    return;
                }
            }
        }
        if (z == 0 || z == 3)
            printf(" |\n");
    }
}


int matrix_det(int matrix[3][3]) {
    int det = 0;

    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
          matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
          matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    return det;
}

void find_roots(int matrix[3][3]) {
    // ax^3 - bx^2 + cx - d = 0
    // a = -sum of the diagonal elements
    // b = sum of the minors of the diagonal element
    // c = -det
    int det = matrix_det(matrix);
    int a = 1;
    int b = -(matrix[0][0] + matrix[1][1] + matrix[2][2]);
    int c = matrix[0][0] * matrix[1][1] + matrix[1][1] * matrix[2][2] + matrix[2][2] * matrix[0][0] -
            matrix[0][1] * matrix[1][0] - matrix[1][2] * matrix[2][1] - matrix[0][2] * matrix[2][0];
    int d = -det;
    /* 
    Cardano's formula to solve cubic equation: a * x^3 + b * x^2 + c * x + d = 0
    p = 3ac - b^2 / 3a^2 
    q = 2b^3 - 9abc + 27a^2d
    Disc = q^2 + (p/3)^3
    
    u =  root 3 (-q/2 + root 2(Disc))
    v =  root 3 (-q/2 - root 2(Disc))
    */
    int p = c / a - (b * b) / (3 * a * a);
    int q = (2 * b * b * b) / (27 * a * a * a) - (b * c) / (3 * a * a) + d / a;
    double discriminant = (q * q) / 4 + (p * p * p) / 27;
    double eigenvalues[3];
    if (discriminant > 0) {
        double u = cbrt(-q / 2 + sqrt(discriminant));
        double v = cbrt(-q / 2 - sqrt(discriminant));
        eigenvalues[0] = u + v - b / (3 * a);
        printf("\nEigenvalue 1: %.2lf\n", eigenvalues[0]);
    } else if (discriminant == 0) {
        double u = cbrt(-q / 2);
        eigenvalues[0] = 2 * u - b / (3 * a);
        eigenvalues[1] = -u - b / (3 * a);
        printf("\nEigenvalue 1: %.2lf\n", eigenvalues[0]);
        printf("Eigenvalue 2: %.2lf\n", eigenvalues[1]);
    } else {
        double rho = sqrt((-p * p * p) / 27);
        double theta = acos(-q / (2 * rho));
        double u = cbrt(rho);
                eigenvalues[0] = 2 * u * cos(theta / 3) - b / (3 * a);
        eigenvalues[1] = 2 * u * cos((theta + 2 * PI) / 3) - b / (3 * a);
        eigenvalues[2] = 2 * u * cos((theta + 4 * PI) / 3) - b / (3 * a);
        printf("\nEigenvalue 1: %.2lf\n", eigenvalues[0]);
        printf("Eigenvalue 2: %.2lf\n", eigenvalues[1]);
        printf("Eigenvalue 3: %.2lf\n", eigenvalues[2]);
    }
}

void matrix_add(int matrix_1[3][3], int matrix_2[3][3]) {
    int temp_matrix[3][3] = {{0}};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            temp_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j];
        }
    }
    matrix_dis(temp_matrix, 0,0);
}

void matrix_sub(int matrix_1[3][3], int matrix_2[3][3]) {
    int temp_matrix[3][3] = {{0}};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            temp_matrix[i][j] = matrix_2[i][j] - matrix_1[i][j];
        }
    }
    matrix_dis(temp_matrix, 0,0);
}

void matrix_mul(int matrix_1[3][3], int matrix_2[3][3]) {
    int temp_matrix[3][3] = {{0}};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                temp_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j];
            }
        }
    }
    matrix_dis(temp_matrix, 0,0);
}

void create_matrix(int y, int z) {
    if (y == 0 && (z == 1 || z == 2 || z == 3)) {
        int matrix_1[3][3] = {{0}};
        int matrix_2[3][3] = {{0}};
        matrix_dis(matrix_1, 1, 1);
        matrix_dis(matrix_1, 3, 1);
        matrix_dis(matrix_2, 1, 2);
        matrix_dis(matrix_2, 3, 2);
        switch (z) {
            case 1:
                printf("\nMatrix Addition:\n");
                matrix_add(matrix_1, matrix_2);
                break;
            case 2:
                printf("\nMatrix Subtraction:\n");
                matrix_sub(matrix_1, matrix_2);
                break;
            case 3:
                printf("\nMatrix Multiplication:\n");
                matrix_mul(matrix_1, matrix_2);
                break;
        }
    } else if (y == 1 && (z == 4 || z == 5)) {
        int matrix[3][3] = {{0}};
        matrix_dis(matrix, 1, 0);
        matrix_dis(matrix, 3, 0);
        switch (z) {
            case 4:
                printf("\nDeterminant: %d\n", matrix_det(matrix));
                break;
            case 5:
                find_roots(matrix);
                break;
            default:
                printf("Invalid operation!\n");
                break;
        }
    }
}

int main() {
    int choice;
    printf("\t\t%10s\t \n", "MatBKix");
    printf("----------------------------------------------------\nSelect any option: \n1.Matrix Addition\n2.Matrix Subtraction\n3.Matrix Multiplication\n4.Matrix determinant\n5.Eigen Values\nOption: ");
    if (scanf("%d", &choice) != 1 || choice < 1 || choice > 5) {
        printf("Invalid input! Please enter a number between 1 and 5.\n");
        return 1;
    }

    switch (choice) {
        case 1:
            create_matrix(0, 1); 
            break;
        case 2:
            create_matrix(0, 2);
            break;
        case 3:
            create_matrix(0, 3); 
            break;
        case 4:
            create_matrix(1, 4);
            break;
        case 5:
            create_matrix(1, 5);
            break;
        default:
            printf("Invalid Option!\n");
            break;
    }
    return 0;
}