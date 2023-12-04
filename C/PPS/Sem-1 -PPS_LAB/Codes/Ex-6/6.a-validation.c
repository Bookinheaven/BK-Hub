#include <stdio.h>
int main() {
    int age;
    // Input age from user
    printf("Enter your age: ");
    scanf("%d", &age);
    // Validate age
    if (age >= 18) {
        printf("You are eligible to vote!\n");
    } 
    else {
        printf("Sorry, you are not eligible to vote.\n");
    } 
    return 0;
}