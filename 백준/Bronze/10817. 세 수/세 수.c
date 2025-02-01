#include <stdio.h>
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if((a>=1)&&(a<=10000)&&(b>=1)&&(b<=10000)&&(c>=1)&&(c<=10000)){
        if(a>=b){
            if(a>=c){
                if(b>=c){printf("%d",b);}
                else{printf("%d",c);}
            }
            else{printf("%d",a);}
		}
		else{
			if(b>=c){
				if(a>=c){printf("%d",a);}
				else{printf("%d",c);}
			}
			else{printf("%d",b);}
		}
	}
	return 0;
  
}
