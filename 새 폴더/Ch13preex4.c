#include<stdio.h>
int main()
{
    int score;
    do {
        printf("점수를 입력하세요(0 ~ 100) : ");
        scanf("%d", &score);
    } while(score < 0 || score > 100);

    printf("입력된 점수 : %d", score);
    return 0;
}
