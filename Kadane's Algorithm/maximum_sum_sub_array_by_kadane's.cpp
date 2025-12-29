#include<iostream>
#include<climits>
using namespace std;
int main(){
    int sum=0;
    int maxvalue=INT_MIN;
    int arr[]={3,-4,5,4,-1,7,-8};
    for(int i=0;i<7;i++){
        sum += arr[i];
        maxvalue=max(sum,maxvalue);
        if(sum<0){
            sum=0;
        }
    }
    cout<<"sum is : "<<maxvalue;
    return 0;
}