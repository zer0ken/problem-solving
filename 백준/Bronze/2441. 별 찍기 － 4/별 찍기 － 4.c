#include <stdio.h>
int main(){
    int N=0,k=0,i=0,q=0;
    scanf("%d",&N);
    if((N>=1)||(N<=100)){
        for(k=N; k>=1; k--){
            for(i=(N-k);i>=1;i--){
                printf(" ");
            }
            for(q=k;q>=1;q--){
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}
