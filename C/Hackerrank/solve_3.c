//https://www.hackerrank.com/challenges/sum-numbers-c/problem?isFullScreen=true
#include <stdio.h>
int main()
{
    int n, m;
    float x, y;

    scanf("%d %d", &n, &m);
    scanf("%f %f", &x, &y);

    printf("%d %d\n",n + m, n - m);
    printf("%.1f %.1f\n", x + y, x - y);

    return 0;
}
/*

Sample Input

10 4
4.0 2.0
Sample Output

14 6
6.0 2.0
*/