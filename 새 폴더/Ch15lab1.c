#include<stdio.h>
int main()
{
    int i, n, sum, result = 1, num;

    printf(" �Է��� ���� : ");
    scanf("%d", &n);


    for(i = 0; i < n; i++) {
        printf("%d��° �� : ", i + 1);
        scanf("%d", &num);

        if(num < 0) break;

        if(num == 0) continue;

        result *= num;
    }
    printf("��갪 : %d", result);
    return 0;
}
