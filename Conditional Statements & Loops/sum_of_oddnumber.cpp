#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter the value of n : ";
    cin>>n;
    int sum=0;
    for(int i=1;i<=n;i=i+2){
        sum=sum+i;
    }
    cout<<"addition is : "<<sum;
}