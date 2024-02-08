#include <stdio.h>
#include <ctype.h>
#include <string.h>

int vowels(char *str,int size){
    int vowles_count = 0;
    for(int i =0 ; i<size; i++){
        char ch = tolower(str[i]);

        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            vowles_count++;
        }
    }
    
    return vowles_count;

}
int main(){
    char arr[]= "helloworld";
    int size = strlen(arr);
    printf("Vowels Count = %d",vowels(arr,size));
    return 0;
}