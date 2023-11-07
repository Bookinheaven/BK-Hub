#include <stdio.h>

const float PI = 3.14;

int circle_area(float radius){
    float area = PI*radius*radius;
    return area;
}
int rectangle_area(float length,float width){
    float area = length*width;
    return area;
}
int square_area(float length){
    float area = length*length;
    return area;
}
int triangle_area(float base, float height){
    float area = (1/2)*(base*height);
    return area;
}

int main(){
    int choice;
    float area;
    printf("I can find areas of these shapes :\n1.Circle\n2.Rectangle\n3.Square\n4.Triangle\nWhat shapes area you want to find? (Enter in numbers): ");
    scanf(" %d",&choice);
    switch (choice) {
    case 1:
        float radius;
        printf("\nYour choice: Circle!");
        printf("\nEnter radius of the circle: ");
        scanf(" %f",&radius);
        area = circle_area(radius);
        break;
    case 2:
        float length, width;
        printf("\nYour choice: Rectangle!");
        printf("\nEnter the value of lenght in the rectangle: ");
        scanf(" %f",&length);
        printf("Enter the value of width in the rectangle: ");
        scanf(" %f",&width);
        area = rectangle_area(length,width);
        break;
    case 3:
        printf("\nYour Choice: Square!");
        printf("\nEnter the value of length in the square: ");
        scanf(" %f",&length);
        area = square_area(length);
        break;
    case 4:
        float base,height;
        printf("\nYour Choice: Triangle!");
        printf("\nEnter the value of base in the triangle: ");
        scanf(" %f",&base);
        printf("\nEnter the value of height in the triangle: ");
        scanf(" %f",&height);
        area = triangle_area(base,height);
        break;
    
    default:
        printf("Invalid choice\n");
        return 1;
    }
    printf("\nArea = %.2f\n",area);
}