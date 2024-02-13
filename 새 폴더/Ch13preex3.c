#include<stdio.h>
int main()
{
    int cnt = 0;
    do {
        printf("%d\n", cnt);
        cnt++;
    }while(cnt <= 5);

    int o = 5;
    do {
        printf("%d\n", o);
        o--;
    }while(o >= 1);
    return 0;
}
