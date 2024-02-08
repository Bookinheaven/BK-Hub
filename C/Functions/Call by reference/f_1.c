#include <stdio.h>
int square(int *num){
    return (*num) * (*num);
}
int main(){

    int num = 12;
    int result = square(&num);
    printf("%d",result);
    return 0;

}