#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> arr = {1,2,4,5};
    int n=5;
    int  sum = 0;
    int sum2 =0;
    sum = (n * (n+1) )/2;
    for(int i=0;i<arr.size();i++){
        sum2 += arr[i];
    }
    cout<<"missing number is "<<sum-sum2;
}