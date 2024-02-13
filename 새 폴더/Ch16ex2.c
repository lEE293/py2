#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int dice1, dice2, i;

    srand((unsigned int)time(NULL));

    for(i = 1; i <= 5; i++) {
        dice1 = rand() % 6 + 1;
        dice2 = rand() % 6 + 1;
        printf("첫번째 주사위 : %d, 두번째 주사위 : %d\n", dice1, dice2);
    }
    return 0;
}
