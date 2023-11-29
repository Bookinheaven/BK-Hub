#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_ITEMS 1000
#define MAX_LINE_LENGTH 1000
#define MAX_FOOD_ITEMS 40
#define MAX_NAME_LENGTH 30

struct Item {
    char Food[MAX_NAME_LENGTH];
    char Measure[20];
    float Grams;
    float Calories;
    float Protein;
    float Fat;
    float Sat_Fat;
    float Fiber;
    float Carbs;
    char Category[MAX_NAME_LENGTH];
};

void display_available_items(struct Item *items, int count) {
    printf("Available Food Items:\n");
    for (int i = 0; i < count; i++) {
        printf("%-3d. %-30s", i + 1, items[i].Food);
        if ((i + 1) % 4 == 0 || i == count - 1) {
            printf("\n");
        } else {
            printf("\t");
        }
    }
    printf("\n");
}

void to_lower(char *str) {
    while (*str) {
        *str = tolower(*str);
        str++;
    }
}

void clean_string(char *str) {
    char *start = str;
    while (*start && isspace(*start)) {
        start++;
    }
    char *end = start + strlen(start) - 1;
    while (end > start && isspace(*end)) {
        *end-- = '\0';
    }
    if (*start == '"') {
        memmove(start, start + 1, strlen(start));
    }
}

void read_data(FILE *file, struct Item **items, int *count) {
    char buffer[MAX_LINE_LENGTH];
    *count = 0;
    *items = (struct Item *)malloc(MAX_ITEMS * sizeof(struct Item));
    if (*items == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    while (*count < MAX_ITEMS && fgets(buffer, sizeof(buffer), file) != NULL) {
        clean_string(buffer);
        sscanf(buffer, "%29[^,], %19[^,], %f, %f, %f, %f, %f, %f, %f, %29[^\n]",
               (*items)[*count].Food, 
               (*items)[*count].Measure, 
               &(*items)[*count].Grams,
               &(*items)[*count].Calories, 
               &(*items)[*count].Protein, 
               &(*items)[*count].Fat,
               &(*items)[*count].Sat_Fat, 
               &(*items)[*count].Fiber, 
               &(*items)[*count].Carbs,
               (*items)[*count].Category);
        to_lower((*items)[*count].Food);
        (*count)++;
    }
}

void check_data(struct Item *items, int count, char initem[MAX_FOOD_ITEMS][MAX_NAME_LENGTH], int num) {
    printf("\nEntered Food Items:\n");
    for (int i = 0; i < num; i++) {
        printf("%d. %s\n", i + 1, initem[i]);
    }
    float totalCalories = 0, totalProtein = 0, totalFat = 0, totalSatFat = 0, totalFiber = 0, totalCarbs = 0;
    printf("\nMatching Items from File:\n");
    int found_match;
    for (int i = 0; i < num; i++) {
        to_lower(initem[i]);
    }
    for (int i = 0; i < count; i++) {
        found_match = 0;
        for (int j = 0; j < num; j++) {
            if (strcmp(items[i].Food, initem[j]) == 0) {
                printf("Match found: %s\n", items[i].Food);
                found_match = 1;
                totalCalories += items[i].Calories;
                totalProtein += items[i].Protein;
                totalFat += items[i].Fat;
                totalSatFat += items[i].Sat_Fat;
                totalFiber += items[i].Fiber;
                totalCarbs += items[i].Carbs;
                break;
            }
        }
        if (!found_match) {
            //printf("No match found for: %s\n", items[i].Food);
            continue;
        }
    }
    float totalPercentage = 0;
    float healthyCalories = 2500;
    float healthyProtein = 50;
    float healthyFat = 70;
    float healthySatFat = 20;
    float healthyFiber = 25;
    float healthyCarbs = 300;
    totalPercentage = ((totalCalories / healthyCalories) +
                       (totalProtein / healthyProtein) +
                       (1 - (totalFat / healthyFat)) +
                       (1 - (totalSatFat / healthySatFat)) +
                       (totalFiber / healthyFiber) +
                       (totalCarbs / healthyCarbs)) / 6.0 * 100;
    printf("\nTotal Nutritional Values of Matched Items:\n");
    printf("Total Calories: %.2f\n", totalCalories);
    printf("Total Protein: %.2f\n", totalProtein);
    printf("Total Fat: %.2f\n", totalFat);
    printf("Total Saturated Fat: %.2f\n", totalSatFat);
    printf("Total Fiber: %.2f\n", totalFiber);
    printf("Total Carbs: %.2f\n", totalCarbs);
    printf("\nPercentage of a Good Diet: %.2f%%\n", totalPercentage);
}

void free_items(struct Item *items) {
    free(items);
}

int main() {
    FILE *food_data = fopen("../nutrients.csv", "r");

    if (food_data == NULL) {
        printf("File not found or unable to open the file\n");
        return 1;
    }

    struct Item *items;
    int count;
    char initem[MAX_FOOD_ITEMS][MAX_NAME_LENGTH];
    
    read_data(food_data, &items, &count);
    display_available_items(items, count);

    int num;
    printf("How many food items do you want to mention?: ");
    scanf("%d", &num);

    
    for (int i = 0; i < num; i++) {
        printf("Enter food item %d: ", i + 1);
        scanf(" %29[^\n]", initem[i]);
        to_lower(initem[i]); 
    }
    
    check_data(items, count, initem, num);

    free_items(items);
    fclose(food_data);

    return 0;
}

/*
Food,       Measure,    Grams,  Calories,   Protein,    Fat,Sat.    Fat,    Fiber,  Carbs,  Category
Cows milk,   1 qt.,     976,    660,        32,         40,         36,      0,     48,     Dairy products
Milk skim,   1 qt.,     984,    360,        36,         t,           t,      0,     52,     Dairy products
*/