#include <stdio.h>
#include <string.h>

int main(){
    char word[20], in_char;
    int i,e,num_letter;
    printf("Want to change a letter in word?\nThen enter the word: ");
    scanf(" %s",word);
    e=strlen(word);
    printf("\nSo now which letter you want to change in this word(len %d) :\"%s\"|\nLetter num: ",e,word);
    scanf(" %d", &num_letter);
    printf("\nFor what char you want to change this letter (%d) to ?: ",num_letter);
    scanf(" %c", &in_char);

    for (i=0; i<=e; i++){
        if (i == num_letter-1){
            word[i] = in_char;
        }
    }
    printf("%s", word);
    

}
