#include <stdio.h>
#include <string.h>
void reverse(char *str) {
    int len = strlen(str);
    int start = 0;
    int end = len-1;

    while (start <end){
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        start++;
        end--;
    }
}

int main(){
    char original[100];
    printf("Enter the string: ");
    scanf("%s", original);

    char reverse_str[100];
    strcpy(reverse_str, original);

    reverse(reverse_str);

    strcat(original,reverse_str);
    printf("Concatenate string: %s",original);
    return 0;
}