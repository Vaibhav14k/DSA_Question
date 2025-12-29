#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter the number"<<endl;;
    cin>>n;
    int flag=1;
    for(int i=2;i<n;i++){
        if(n%i==0){
            flag=0;
            break;
        }
    }
    if(flag){
        cout<<"prime";
    }else{
        cout<<"not prime";
    }
}