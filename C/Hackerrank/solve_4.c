//https://www.hackerrank.com/challenges/functions-in-c/problem?isFullScreen=true
#include <stdio.h>

int max_of_four(int a, int b, int c, int d){
    int ans = a;
    if(b > ans){
        ans = b;
    }
    if(c > ans){
        ans = c;
    }
    if(d > ans) {
        ans = d;
    }
    return ans;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
/*
Sample Input

3
4
6
5
Sample Output

6
*/