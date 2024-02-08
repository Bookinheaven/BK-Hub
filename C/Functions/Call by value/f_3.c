/*
C Program to Find All Roots of a Quadratic Equation
*/

#include <stdio.h>
#include <math.h>
void find_roots(float discri,float a,float b,float c){ //function declaration
    float fin_root=0;
    if(discri>0){
        fin_root = -b+sqrt(pow(b,2)-(4*a*c));//function definition
        printf("Root :%.2f",fin_root);
    }
    else if(discri==0){
        fin_root = -b-sqrt(pow(b,2)-(4*a*c));
        printf("Root :%.2f",fin_root);
    }
    else{
        float real,imaginary;
        real = -b/(2*a);
        imaginary = sqrt(-discri)/(2*a);
        printf("Root 1:%.2f+i%.2f\nRoot 2:%.2f-i%.2f",real,imaginary,real,imaginary);

    }
}
void func_discri(float a, float b, float c){
    float d =(-pow(b,2)-4*a*c);
    find_roots(d,a,b,c);// function call---> d,a,b,c is arguments
}

int main(){

    /* 
    discriminent-b^2-4ac 
    >0  -b+sqw(b^2-4ac)/2a
    =0 -b-sqw(b^2-4ac)/2a
    <0 rt1 = -b/2a + i sqr(-(b^2-4ac))/2
    <0 rt2 = -b/2a - i sqr(-(b^2-4ac))/2
    */
    float a=0, b=0, c=0;
    printf("Enter Values of a b c: ");
    scanf(" %f %f %f", &a,&b,&c);
    func_discri(a,b,c);
    return 0;
}