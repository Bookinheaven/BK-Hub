#include <stdio.h>
char calculateGrade(float marks){
    if (marks >= 90){
        return 'A';
    }
    else if (marks >= 80){
        return 'B';
    }
    else if (marks >= 70){
        return 'C';
    }
    else if (marks >= 60){
        return 'D';
    }
    else{
        return 'F';
    }
}
int main()
{
    float subjectMarks[5],totalMarks = 0.0,averageMarks;
    printf("Enter the marks for five subjects:\n");
    for (int i = 0; i < 5; i++){
        printf("Subject %d: ", i + 1);
        scanf("%f", &subjectMarks[i]);
        totalMarks += subjectMarks[i];
    }
    averageMarks = totalMarks / 5;
    printf("\nGrades for each subject:\n");
    for (int i = 0; i < 5; i++){
        printf("Subject %d: %c\n", i + 1, calculateGrade(subjectMarks[i]));
    }
    printf("\nAverage Marks: %.2f\n", averageMarks);
    printf("Grade: %c\n", calculateGrade(averageMarks));
    return 0;
}