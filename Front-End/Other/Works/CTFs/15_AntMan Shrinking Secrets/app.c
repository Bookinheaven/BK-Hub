#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char encoded_passphrase[] = "eW91J3JlIHRoZSByaWdodCBtYW4gZm9yIHRoZSBqb2I=";

char encoded_flag[] = "ZTAxRFgwTlVSanBCYm5STllXNWZTVzVmVkdobFgwTnZaR1Y5";

void fake_loading() {
    printf("\nRetrieving encrypted SHIELD directive...\n");
    sleep(2);
    printf("\nEncrypted Message: %s\n", encoded_flag);
    printf("\nHINT: Sometimes things need to be undone **twice** before they reveal the truth.\n");
}

int main() {
    char input[100];

    printf("\nPym Technologies Secure Terminal v2.0 \n");
    printf("--------------------------------------------------\n");
    printf("Welcome to Ant-Man's Micro Code Challenge! \n");
    printf("Enter the correct passphrase to restore the suit:\n");

    int attempts = 0;
    while (1) {
        printf("> ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0;  

        if (strcmp(input, "you're the right man for the job") == 0) {
            printf("\n✅ Access granted! Restoring the suit...\n");
            fake_loading();
            break;
        } else {
            attempts++;
            printf("❌ ACCESS DENIED. Try again.\n");

            if (attempts == 3) {
                printf("\n💡 HINT: Hank Pym chose Scott for a reason. What did he say to him?\n");
            } else if (attempts == 5) {
                printf("\n🚨 WARNING: Too many failed attempts! PymTech security is watching...\n");
            } else if (attempts == 7) {
                printf("\n⛔ SYSTEM LOCKED. Restart the terminal.\n");
                exit(0);
            }
        }
    }

    printf("\nPress Enter to exit...");
    getchar();
    return 0;
}
