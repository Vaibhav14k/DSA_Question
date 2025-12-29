#include<iostream>
using namespace std;
int main(){
    int sum=0;
    int n=7;
    int maxsum=0;
    int arr[]={3,-4,5,4,-1,7,-8};
    for(int i=0;i<n;i++){
        int currentsum=0;
        for(int j=i;j<n;j++ ){
            currentsum += arr[j];
            maxsum=max(currentsum,maxsum);
        }
        cout<<endl;
    }
    cout<<"maximu sum is : "<<maxsum;
    return 0;
}