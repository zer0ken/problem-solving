#include <stdio.h>
int main(){
    int N=0,k=0,i=0;
    scanf("%d",&N);
    if(N>=1)
    {
        if(N<=100)
        {
            for(k=1; k<=N; k++)
            {
                for(i=1; i<=k; i++)
                    printf("*");
                printf("\n");
            }
        }
    }
    return 0;
 }