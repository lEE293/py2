#include<stdio.h>
int main()
{
    int n, r, i, sum;
    printf("정수를 입력하세요 : ");
    scanf("%d", &n);

    printf("거듭제곱을 입력하세요 : ");
    scanf("%d", &r);

    sum = 1;
    for( i = 1; i <= r; i++ ) {
        sum *= n;
    }
    printf("%d의 %d 승은 %d입니다", n, r, sum);
    return 0;
}
