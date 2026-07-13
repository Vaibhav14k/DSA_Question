#include<iostream>
using namespace std;
int main(){
    int n;
cout<<"enter the n number : ";
cin>>n;
for (int i=2;i<n;i++){
    if (n%i==0){
        cout<<"n is not an prime number  :\n ";
        break;
    }
    else{
        cout<<"n is an prime number ";
        break;
    }
}
}
