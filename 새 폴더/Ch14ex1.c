#include<stdio.h>
int main()
{
    int i, max, min, num;

    max = 0;
    min = 100;

    for( i = 0; i < 5; i++) {
        printf("%d��°�� ���ڸ� �Է��ϼ���< 1 ~ 100 > : ", i + 1);
        scanf("%d", &num);

        if( num > max ) max = num;
        if( num < min ) min = num;
    }
    printf("�ִ밪 : %d, �ּڰ� : %d", max, min);
    return 0;
}
