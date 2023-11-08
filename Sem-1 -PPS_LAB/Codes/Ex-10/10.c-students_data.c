#include <stdio.h>
#include <stdlib.h>

struct Student {
    char name[50];
    int rollNumber;
    float marks;
};

void storeStudentDetails(FILE *file) {
    struct Student student;
    printf("Enter student name: ");
    scanf("%s", student.name);
    printf("Enter roll number: ");
    scanf("%d", &student.rollNumber);
    printf("Enter marks: ");
    scanf("%f", &student.marks);
    
    fprintf(file, "Name: %s\nRoll Number: %d\nMarks: %.2f\n\n", student.name, student.rollNumber, student.marks);
    
    printf("Student details stored successfully.\n");
}

void displayStudentDetails(FILE *file) {
    struct Student student;
    printf("Student Details:\n");
    while (fscanf(file, "Name: %s\nRoll Number: %d\nMarks: %f\n", student.name, &student.rollNumber, &student.marks) != EOF) {
        printf("Name: %s\n", student.name);
        printf("Roll Number: %d\n", student.rollNumber);
        printf("Marks: %.2f\n\n", student.marks);
    }
}

int main() {
    int choice;
    do {
        printf("1. Store Student Details\n");
        printf("2. Display Student Details\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        FILE *file;
        file = fopen("student_details.txt", "a+");

        if (file == NULL) {
            printf("Error opening the file.\n");
            return 1;
        }

        switch (choice) {
            case 1:
                storeStudentDetails(file);
                fclose(file);
                break;
            case 2:
                displayStudentDetails(file);
                fclose(file);
                break;
            case 3:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}
