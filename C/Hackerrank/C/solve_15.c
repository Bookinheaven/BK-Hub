//https://www.hackerrank.com/challenges/printing-tokens-/problem?isFullScreen=true
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    //Write your logic to print the tokens of the sentence here.
    for(int i=0; i<strlen(s); i++){
        if(s[i] != ' '){
            printf("%c", s[i]);
        }
        else {
            printf("\n");
        }
        
    }
    return 0;
}
/*
Sample Input 0

This is C 
Sample Output 0

This
is
C
Explanation 0

In the given string, there are three words ["This", "is", "C"]. We have to print each of these words in a new line.

Sample Input 1

Learning C is fun
Sample Output 1

Learning
C
is
fun
Sample Input 2

How is that
Sample Output 2

How
is
that
*/