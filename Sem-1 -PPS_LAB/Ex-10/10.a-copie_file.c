#include <stdio.h>
int main() {
    FILE *sourceFile, *destFile;
    char ch;

    sourceFile = fopen("../source.txt", "r"); // Open the source file in read mode
    if (sourceFile == NULL) {
        perror("Error opening source file");
        return 1;
    }

    destFile = fopen("../destination.txt", "w"); // Open the destination file in write mode
    if (destFile == NULL) {
        perror("Error opening destination file");
        fclose(sourceFile); // Close the source file before exiting
        return 1;
    }

    while ((ch = fgetc(sourceFile)) != EOF) {
        fputc(ch, destFile); // Write each character from the source to the destination
    }

    printf("File copied successfully!\n");

    fclose(sourceFile);
    fclose(destFile);

    return 0;
}
