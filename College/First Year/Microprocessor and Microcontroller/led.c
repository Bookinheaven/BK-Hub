#include <reg51.h>
sbit led1=P0^0;
sbit led2=P0^1;
sbit led3=P0^2;
sbit led4=P0^3;
sbit led5=P0^4;
sbit led6=P0^5;
sbit led7=P0^6;
sbit led8=P0^7;
sbit switch1=P2^0;
sbit switch2=P2^1;
sbit switch3=P2^2;
sbit switch4=P2^3;
sbit switch5=P2^4;
sbit switch6=P2^5;
sbit switch7=P2^6;
sbit switch8=P2^7;
void main()
{
P0=0X00;
P2=0Xff;
while(1)
{
if (switch1==0)
{
led1=0;led2=1;led3=1;led4=1;led5=1;led6=1;led7=1;led8=1;
}
else if (switch2==0)
{
led1=1;led2=0;led3=1;led4=1;led5=1;led6=1;led7=1;led8=1;
}
else if (switch3==0)
{
led1=1;led2=1;led3=0;led4=1;led5=1;led6=1;led7=1;led8=1;
}
else if (switch4==0)
{
led1=1;led2=1;led3=1;led4=0;led5=1;led6=1;led7=1;led8=1;
}
else if (switch5==0)
{
led1=1;led2=1;led3=1;led4=1;led5=0;led6=1;led7=1;led8=1;
}
else if (switch6==0)
{
led1=1;led2=1;led3=1;led4=1;led5=1;led6=0;led7=1;led8=1;
}
else if (switch7==0)
{
led1=1;led2=1;led3=1;led4=1;led5=1;led6=1;led7=0;led8=1;
}
else if (switch8==0)
{
led1=1;led2=1;led3=1;led4=1;led5=1;led6=1;led7=1;led8=0;
}
}
}