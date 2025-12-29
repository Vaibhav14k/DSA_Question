#include<iostream>
using namespace std;
int main(){
    char n;
    cout<<"enter the char n:";
    cin>>n;
    int a=(int)n;
    cout<<a;
    if(a>=65  &&  a<90 ){
        cout<<" is upper case : ";
    }
    else if (a>=95 && a<120){
        cout<<"it is lower case : ";
        
    }
    return 0;
}