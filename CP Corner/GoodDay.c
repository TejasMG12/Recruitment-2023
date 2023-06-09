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
     int s=0,r=0;
    char a[15];
    fgets(a, sizeof(a), stdin); 
    for (int i=0;i<15;i++){   
        if (a[i]=='1')
        s++;
        if (a[i]=='0')
        r++;  
    }
    s>r?printf("YES"):printf("NO");
    return 0;
}

