#include<stdio.h>
int main()
{
    int score;
    do {
        printf("������ �Է��ϼ���(0 ~ 100) : ");
        scanf("%d", &score);
    } while(score < 0 || score > 100);

    printf("�Էµ� ���� : %d", score);
    return 0;
}
