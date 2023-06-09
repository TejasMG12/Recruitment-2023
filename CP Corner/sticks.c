#include "stdio.h"
int main()
{
    int a,b;
    
    scanf("%d%d%",&a,&b);
    if (a%b==0)
    printf("YES");
    else if ((a%b)%2==b%2)
        printf("Yes");
    else
    printf("NO");

    return 0;
}
