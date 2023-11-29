#include <stdio.h>
struct list_persons {
    char name[20];
    int age;
};
int main(){
    struct list_persons person[2];
    for (int i = 0; i < 2; i++) {
        printf("Enter name, age of each person %d: ", i + 1);
        scanf("%s %d", person[i].name, &person[i].age);
    }
    for (int i = 0; i < 2; i++) {
        printf("Person %d - Name: %s, Age: %d\n", i + 1, person[i].name, person[i].age);
    }
    return 0;
}