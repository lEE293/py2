#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int num, i;
    srand((unsigned int) time(NULL));

    printf("난수 출력 : ");

    for( i = 1; i <= 10; i++) {
        num = rand() % 100 + 1;
        printf(" %d", num);
    }


    return 0;
}
