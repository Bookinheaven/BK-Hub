#include <reg51.h>
#include <stdio.h>
#define DLY 1000

sbit s_d0 = P2^7;
sbit s_d1 = P2^6;
sbit s_d2 = P2^5;
sbit s_d3 = P2^4;

void main() {
unsigned int i;
while(1){
for (i=0; i<=DLY; i++);
s_d0 = 0;
s_d1 = 1;
s_d2 = 1;
s_d3 = 1;

for (i=0; i<=DLY; i++);
s_d0 = 1;
s_d1 = 0;
s_d2 = 1;
s_d3 = 1;

for (i=0; i<=DLY; i++);
s_d0 = 1;
s_d1 = 1;
s_d2 = 0;
s_d3 = 1;

for (i=0; i<=DLY; i++);
s_d0 = 1;
s_d1 = 1;
s_d2 = 1;
s_d3 = 0;

}
}