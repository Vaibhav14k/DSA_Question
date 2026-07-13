#include<iostream>
using namespace std;
int main(){
    int fre=0;
    int ans=0;
    int arr[]={1,2,2,2};
    for (int i=0;i<4;i++){
        if (fre=0){
            ans = arr[i];
        }
        else if( ans == arr[i]){
            fre++;
        }
        else{
            fre--;
        }
    }
}