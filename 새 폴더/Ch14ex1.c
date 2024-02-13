#include<stdio.h>
int main()
{
    int i, max, min, num;

    max = 0;
    min = 100;

    for( i = 0; i < 5; i++) {
        printf("%d번째의 숫자를 입력하세요< 1 ~ 100 > : ", i + 1);
        scanf("%d", &num);

        if( num > max ) max = num;
        if( num < min ) min = num;
    }
    printf("최대값 : %d, 최솟값 : %d", max, min);
    return 0;
}
