//https://www.hackerrank.com/challenges/playing-with-characters/problem?isFullScreen=true
#include <stdio.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    char ch = '\0',s[15]={0},sen[50]={0};
    scanf("%c",&ch);
    printf("%c\n",ch);
    scanf("%s",s);
    scanf("\n");
    printf("%s\n",s);
    scanf("%[^\n]%*c",sen);
    printf("%s\n",sen);
    return 0;
}
/*
Sample Input 0

C
Language
Welcome To C!!

Sample Output 0

C
Language
Welcome To C!!
*/