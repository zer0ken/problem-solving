#include<stdio.h>
int main(){
    int N,k,result=1;
    scanf("%d",&N);
    if(N==0){result=1;}
    else if(N>0&&N<=12){
        for(k=1;k<=N;k++){
            result*=k;
        }
    }
    if(N>=0&&N<=12){
        printf("%d",result);
    }
    return 0;
}