#include <reg51.h>

void Delay(){
TMOD = 0x01;
TL0 = 0x00;
TH0 = 0xEE;
TR0 = 1;
while (TF0 == 0);
TR0 = 0;
TF0 = 0;
}

void main(){
P1 = 0xAA;
Delay();
P1 = 0x00;
Delay();
}
