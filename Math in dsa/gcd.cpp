#include<iostream>
using namespace std;
int gdc(int a,int b){
    while ( a>0 && b>0 ){
        if (a>b){
            a=a%b;
        }
        else { b=b%a;
           }   }
    if(a==0) return b;
    return a;
}
int main(){
    cout<<gdc(20,28);
    return 0;
}