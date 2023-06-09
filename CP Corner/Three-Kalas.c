#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main()
{
    int a,b,c,d;
    char x;
    scanf("%d%c%d%c%d%c%d",&a,&x,&b,&x,&c,&x,&d);
    if (a==d || b==d || c==d )
    printf("Yes");
    else
    printf("No");

    return 0;
}

