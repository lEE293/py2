#include<stdio.h>
int main()
{
    int n, sum = 0;

    do {
        printf("정수를 입력하세요 : ");
        scanf("%d", &n);
        sum += n;

    } while(n != 0);
    printf("합계는 %d입니다\n", sum);
    return 0;
}
