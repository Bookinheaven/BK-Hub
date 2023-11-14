//https://www.hackerrank.com/challenges/pointer-in-c/problem?isFullScreen=true
#include <stdio.h>

void update(int *a,int *b) {
    int a_a = *a + *b;
    int b_b = *a - *b;
    if (b_b <0){
        *b = -b_b;
        *a = a_a;
    }
    else{
        *b = b_b;
        *a = a_a;
    }
    
    return;
     
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
/*
Sample Input

4
5
Sample Output

9
1
*/
