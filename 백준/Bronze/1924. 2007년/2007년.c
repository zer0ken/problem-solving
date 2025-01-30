#include <stdio.h>
int Censorship(int M,int D);
int main(){
    int Mx=0,Dy=0,k=0,R=0,Sum=0;
    scanf("%d %d",&Mx,&Dy);
    if(((Mx>=1)&&(Mx<=12))&&((Dy>=1)&&(Dy<=31))){
       for(k=1;k<Mx;k++){
           if(k<=7){
               if(k==2){Sum+=28;}
               else if(k%2==1){Sum+=31;}
               else if(k%2==0){Sum+=30;}
           }
           else if(k>=8){
               if(k%2==1){Sum+=30;}
               else if(k%2==0){Sum+=31;}
           }
       }
    }
    if(Censorship(Mx,Dy)!=0){
        Sum+=Dy,R=Sum%7;
        if(R==0){printf("SUN");}
        else if(R==1){printf("MON");}
        else if(R==2){printf("TUE");}
        else if(R==3){printf("WED");}
        else if(R==4){printf("THU");}
        else if(R==5){printf("FRI");}
        else if(R==6){printf("SAT");}
    }
    return 0;
}
int Censorship(int M, int D){
    int m_d=1;
    if(M<=7){
        if((M==2)&&(D>28)){m_d=0;}
        else if((M%2==1)&&(D>31)){m_d=0;}
        else if((M%2==0)&&(D>30)){m_d=0;}
    }
    else if(M>=8){
        if((M%2==1)&&(D>30)){m_d=0;}
        else if((M%2==0)&&(D>31)){m_d=0;}
    }
    return m_d;
}
