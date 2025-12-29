#include<iostream>
using namespace std;
int main(){
    int small=20;
    int arr[5]={10,12,5,12,6};
    for(int i=0;i<5;i++){
        if(arr[i]<small){
            small = arr[i];
        }
    }
    cout<<"smallest value in the array is  : "<<small<<endl;
    return 0;
}