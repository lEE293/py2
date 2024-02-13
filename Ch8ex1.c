#include<stdio.h>
int main()
{
    int cnt = 0;

    cnt  += 1;
    printf("cnt = %d \n", cnt);
    printf("cnt = %d \n", cnt+=1);
    printf("cnt = %d \n", cnt+1);
    printf("cnt = %d \n", cnt+1);

    printf("cnt = %d \n", cnt+=2 ); //4
    printf("cnt = %d \n", cnt-1);  //3
    printf("cnt = %d \n", cnt); //4
    return 0;
}
