#include<iostream>
using namespace std;
int main(){
    int arr[]={2,7,11,15};
    for( int i=0;i<4;i++){
        for(int j=i+1;j<4;j++){
            cout<<" ( "<<arr[i]<<","<<arr[j]<<")";
        }
        cout<<endl;
    }
}