#include<stdio.h>
int main()
{
    int i, dan;

    printf("����� ���� �Է��ϼ��� : ");
    scanf("%d", &dan);

    for( int i = 1; i <= 10; i++) {
        printf(" %d * %d = %d\n", dan , i , dan * i);
    }
    return 0;
}
