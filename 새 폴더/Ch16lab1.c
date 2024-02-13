#include<stdio.h>

int main()
{
    int ch;
    printf("문자 하나를 입력하세요\n");
    ch = getchar();

    if(isalpha(ch) {

    if(islower(ch)) {
        printf("%c는 소문자입니다", ch);
    }

    else if(isdigit(ch)) {
        printf("%d는 숫자입니다", ch);
    }

    else {
        printf("%c는 대문자입니다", ch);
    }

}
    return 0;
}
