#include <stdio.h>
#include <string.h>

struct person {
    char name[20];
    int number;
    int age;
};
//} p_1,p_2;
int main(){
    struct person p_1;

    strcpy(p_1.name, "Burn");
    p_1.age = 12;
    p_1.number = 32322;
    printf("Name: %s, Age: %d, Number: %d\n", p_1.name, p_1.age,p_1.number);

    return 0;
    
}