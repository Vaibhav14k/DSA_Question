#include<iostream>
using namespace std;
// target = 10
int main(){
    int arr[]={1,2,3,4,5};
    for(int i=0;i<5;i++){
        // int a=arr[i]+arr[i+1];
        if ( arr[i]+arr[i+1] ==9  ) {
            cout<<arr[i]<< " " <<arr[i+1]<<" ";
            break;
        }
    }
    return 0;
}