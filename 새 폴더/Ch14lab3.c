#include<stdio.h>
int main()
{
    int n, r, i, sum;
    printf("������ �Է��ϼ��� : ");
    scanf("%d", &n);

    printf("�ŵ������� �Է��ϼ��� : ");
    scanf("%d", &r);

    sum = 1;
    for( i = 1; i <= r; i++ ) {
        sum *= n;
    }
    printf("%d�� %d ���� %d�Դϴ�", n, r, sum);
    return 0;
}
