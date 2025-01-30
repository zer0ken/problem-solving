#include <stdio.h>
int main(){
    unsigned int arr[10000];
    unsigned int len,xx,in,k;
    scanf("%d %d",&len,&xx);
    if(len>=1&&len<=10000&&xx>=1&&xx<=10000){
        for(k=0;k<len;k++){
            scanf("%d",&in);
            if(in>=1&&in<=10000){
                arr[k]=in;
            }
        }
        for(k=0;k<len;k++){
            if(arr[k]<xx){
                printf("%d ",arr[k]);
            }
        }
    }
    return 0;
}
