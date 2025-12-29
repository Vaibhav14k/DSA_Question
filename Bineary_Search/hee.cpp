#include<iostream>
#include<vector>
#include <limits.h>
using namespace std;
bool ispossible( vector<int>arr,int n, int m,int maxAllowetime ){
    int painter = 0, time = 0;
    for (int i=0;i<n;i++){
        if (time + arr[i]<=maxAllowetime  ){
            time = time + arr[i];
        }
        else {
            painter++;
            time = arr[i];
        }
    }
    return  painter <=m ;
}

int minitime(vector<int>arr,int n,int m){
    int sum = 0;
    int maxval=INT_MIN;
    for (int i=0;i<n;i++){
        sum = sum + arr[i];
        maxval = max(arr[i],maxval);
    }
    int st = maxval;
    int end = sum;
    while (st<=end)
    {
        int mid = st + (end -st)/2;
        if (ispossible(arr,n,m,mid)){ // true
            int ans = mid;
            end = mid -1;
        }
        else {
            st = mid + 1;
        }
    }
    
}
int main(){
    vector<int>arr ={40,30,10,20};
    int n=4 ,m=2;
    cout<<minitime(arr,n,m)<<endl;
}