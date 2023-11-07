#include <stdio.h>

int main() {
    int i,j,x,rows;
    printf("Input number of rows: ");
    scanf("%d",&rows);
    for(i=1;i<=rows;i++){
        for(j=1;j<=i;j++){
            x+=1;
            printf("%d ",x);
        }
        printf("\n");
    }
    return 0;
}