#include <stdio.h>
#include <string.h>
int main() {
    int marks;
    char grade[3]; 

    printf("Enter Your Marks: ");
    scanf("%d", &marks);

    if (marks == 100) {
        strcpy(grade, "A+"); 
    }
    else if (marks >= 90 && marks <= 99) {
        grade[0] = 'A';
    }
    else if (marks >= 80 && marks <= 89) {
        grade[0] = 'B';
    }
    else if (marks >= 70 && marks <= 79) {
        grade[0] = 'C';
    }
    else if (marks >= 51 && marks <= 69) {
        grade[0] = 'D';
    }
    else if (marks <= 50) {
        grade[0] = 'F';
    }

    printf("Your Grade: %s", grade);

    return 0;
}
