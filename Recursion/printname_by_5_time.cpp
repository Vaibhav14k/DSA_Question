#include<iostream>
using namespace std;
void name(int i,int n) {
    if(i>n){
        return;
    }
    cout<<"vaibhav"<<endl;
    name(i+1,n);
}

int main(){
    int n;
    cin>>n;
    name(0,n) ;
    return 0;
}