#include <stdio.h>
#include <string.h>
int main(){
    char str[50]="tutorial", temp;
    int initial, end, len;
    printf(" Given String = %s \n", str);
    len = strlen(str);
    end = len - 1;
    for (initial=0; initial < end; initial++) {
        temp = str[initial];
        str[initial] = str[end];
        str[end] = temp;
        end--;
    }
    printf(" Reversed String = %s ", str);
    return 0;
    }