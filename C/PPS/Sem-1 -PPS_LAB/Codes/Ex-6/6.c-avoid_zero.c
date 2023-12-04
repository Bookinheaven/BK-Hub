#include <stdio.h>
int main(){
    int a,b;
    float c;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    
    if (b==0){
        printf("-_- Can't Divide by 0!");
    }
    else {
        c =(float)a/b;
        printf("Value: %.2f",c);
    }
    return 0;

}