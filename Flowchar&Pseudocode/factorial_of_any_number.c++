#include<iostream>
using namespace std;
int main(){
    int n,total=1;
    cout<<"enter the value of n : ";
    cin>>n;
    for(int i=1; i<=n;i++){
        total=total*i;
    }
    cout<<"factorial is : "<<total;
}