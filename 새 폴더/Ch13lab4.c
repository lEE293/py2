#include<stdio.h>
int main()
{
    int n, sum = 0;

    do {
        printf("������ �Է��ϼ��� : ");
        scanf("%d", &n);
        sum += n;

    } while(n != 0);
    printf("�հ�� %d�Դϴ�\n", sum);
    return 0;
}
