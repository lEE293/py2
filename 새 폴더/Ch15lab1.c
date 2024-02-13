#include<stdio.h>
int main()
{
    int i, n, sum, result = 1, num;

    printf(" 입력의 개수 : ");
    scanf("%d", &n);


    for(i = 0; i < n; i++) {
        printf("%d번째 수 : ", i + 1);
        scanf("%d", &num);

        if(num < 0) break;

        if(num == 0) continue;

        result *= num;
    }
    printf("계산값 : %d", result);
    return 0;
}
