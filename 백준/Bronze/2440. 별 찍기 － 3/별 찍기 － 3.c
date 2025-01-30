#include <stdio.h>
int main(){
    int N=0,k=0,i=0;
    scanf("%d",&N);
    if(N>=1)
    {
        if(N<=100)
        {
            for(k=0; k<N; k++)
            {
                for(i=N-k; i>0; i--)
                    printf("*");
                printf("\n");
            }
        }
    }
    return 0;
 }