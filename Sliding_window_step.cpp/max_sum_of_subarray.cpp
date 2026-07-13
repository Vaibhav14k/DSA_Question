#include<iostream>
#include<vector>
using namespace std;
int maxSumSubarray(vector<int>& nums,int k){
    int n=nums.size();
    int window=0;
    for(int i=0;i<k;i++){
        window = window + nums[i];
    }
    int maxwindow =0 ;
    for(int i=k;i<n;i++){
        window += nums[i] - nums[i-k];
        maxwindow = max(maxwindow,window);
    }
    return maxwindow;
}   
int main(){
    
    vector<int> arr = {2, 1, 5, 1, 3, 2};
    int k = 3;
    cout << "Maximum sum of subarray of size " << k << " = "
    << maxSumSubarray(arr, k) << endl;
    return 0;
}