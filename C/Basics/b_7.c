/*
C Program to Print the ASCII Value of a Character
*/

#include <stdio.h>

int main(){
    char x;
    printf("Enter the letter: ");
    scanf("%c", &x);
    printf("ASCII of \"%c\" is \'%d\'", x,x);
    return 0;
}