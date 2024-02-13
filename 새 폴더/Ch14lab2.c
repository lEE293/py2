#include<stdio.h>
int main()
{
    int a, b , i;

    printf("정수 2개를 입력하세요(작은 수 큰 수 순서로) : ");
    scanf("%d %d", &a, &b);

    for( i = a; i <= b; i++) {
        if( i % 2 == 1)
            printf("%d\n", i);
    }
    return 0;
}
