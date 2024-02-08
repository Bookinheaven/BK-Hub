/*
C Program to Find G.C.D Using Recursion
*/
#include <stdio.h>
/*
Euclidean Theory
GCF wont change even if you subtract continuously from largest number and smallest number 
*/

int gcf(int num_1,int num_2){//function declaration
    if(num_1 ==0){//function definition
        return num_2;
    }
    if(num_1 < num_2){
        //return gcf(num_2-num_1,num_1);
        return gcf(num_2%num_1,num_1);
    }
    else{
        return gcf(num_1%num_2,num_2);
        //return gcf(num_1-num_2,num_2);
    }
}
int main(){
    int num_1=0,num_2 =0,result=0;
    printf("Enter two numbers: ");
    scanf(" %d %d",&num_1,&num_2);
    if(num_1<0 || num_2 <0){
        return printf("Can't Find for negetive numbers");
        
    }
    result = gcf(num_1,num_2);// function call---> num_1,num_2 is arguments
    printf("GCF of \"%d\" , \"%d\": %d",num_1,num_2,result);
    return 0;


}