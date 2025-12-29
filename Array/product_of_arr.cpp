#include<iostream>
using namespace std;
int main(){
    int arr[]={1,2,1,1,1};
    int product=1;
    for(int i=0;i<5;i++){
        product = product*arr[i];
    }
    cout<<product;
}