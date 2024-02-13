#include<stdio.h>
#include<ctype.h>
int main()
{
    int ch;

    while(1) {
        ch = getchar();
        if( ch == EOF) break;
        if( islower(ch) ) {
            ch = toupper(ch);
        }
        putchar(ch);
    }
    return 0;
}
