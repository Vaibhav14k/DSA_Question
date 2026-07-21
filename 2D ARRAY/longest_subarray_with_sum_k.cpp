#include<iostream>
#include<vector>
using namespace std;
int lonest_subarray(vector<int> num , int k){
    int n= num.size();
    int right =0;
    int left =0;
    int sum =0;
    int maxl=0;
    while(right < n){
        if(sum > k){
            sum -= num [left];
            left ++;
        }
        if(sum == k) maxl = max (maxl, right -left + 1);
        right ++;
        sum += num [right];
    }
    return maxl;
}
int main(){
    vector<int> num = {1,2,3,1,1,1,1,4};
    int k=3;
    cout<<lonest_subarray(num,k);
    
}