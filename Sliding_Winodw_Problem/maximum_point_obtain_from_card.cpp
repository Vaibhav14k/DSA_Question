#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>arr = { 6,2,3,4,7,2,1,7,1};
    int k=4;
    int n = arr.size();
    int lsum=0;
    int rsum=0;
    int total=0;
    for(int i=0;i<=k-1;i++){
        lsum = lsum+  arr[i];
    }
    cout<<"lsum :"<<lsum<<endl;
    total = lsum;
    int r=n-1;
    for(int i=k-1; i>=0;i--){
        lsum -= arr[i];
        rsum += arr[r];
        r--;
        total = max(total,rsum + lsum);
    }
    cout<<"total "<<total<<endl;
}