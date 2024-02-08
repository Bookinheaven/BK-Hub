#include <stdio.h>
#include <string.h>

int main(){
    char word[20],palindrom_word[20]={0};
    int i,e;
    printf("Want to check your word is a palindrom or not?\nThen enter the word: ");
    scanf("%s",word);
    printf("So you want to check palindrom for this word \"%s\"!", word);
    e=strlen(word)-1;
    for(i=0; i<=e; i++){
        palindrom_word[i] = word[e-i];
    }
    if (strcmp(word,palindrom_word) == 0){ 
        printf("\nWord : \"%s\" is a palindrom!",word);
    }
    else {
        printf("\nWord : \"%s\" is not a palindrom!",word);
    }
    return 0;
    
}