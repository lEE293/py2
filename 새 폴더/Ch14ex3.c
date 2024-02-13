#include<stdio.h>
int main()
{
    for( int dan = 1; dan <= 10; dan++) {
        for( int i = 1; i <= 10; i++) {
        printf(" %d * %d = %d\n", dan , i , dan * i);
      }
      printf("\n");
    }
    return 0;
}
