#include <stdio.h>
#include <string.h>

int main() {
    char input[50];
    char da[] = "You Ever Try to Remember Something and Just Couldn't?";
    char db[] = "Don't be what they made you.";
    char dc[] = "Your Best Is Enough. Trust Me.";
    char dd[] = "But Bein' a Man...That Means Choosin' to Grow an' Change An' Put Aside the Old Ways.";
    char de[] = "Grow Those Back.";
    char df[] = "Nature Made Me A Freak. Man Made Me A Weapon.";
    char dg[] = "I'm A Soldier, And I've Been Hiding Too Long.";
    char dl[] = "I’m The Best There Is At What I Do, But What I Do Best Isn’t Very Nice.";
    
    printf("Enter the secret passphrase: ");
    scanf("%s", input);

    if (strcmp(input, "So... This Is What It Feels Like.") == 0) {
        printf("Well done!, enter 'data.txt' in the input field \n");
    } else {
        printf("Access Denied.\n");
    }

    return 0;
}
