#include <stdio.h>
#include <string.h>

int main(){
    char word [50]="", largest_word[50]="";
    int num_words = 0, largest_word_length=0;
    FILE *wordsfile;
    wordsfile = fopen("../words.txt", "r");
    if (wordsfile == NULL){
        perror("I Can't find the file...");
    }
    else {
        while(fscanf(wordsfile, "%s",word) != EOF){
            num_words++;
            int current_words_length = strlen(word);
            if (current_words_length > largest_word_length){
                largest_word_length = current_words_length;
                strcpy(largest_word, word);
            }
        }
        printf("Words found : |%d|\nLargest Lenght: {%d}\nWord: [%s]\n",num_words,largest_word_length,largest_word);
    }
    fclose(wordsfile);
    return 0;
}