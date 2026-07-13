#include<iostream>
#include<vector>
using namespace std;
int product(vector<int> & nums){
    vector<int>ans(nums.size());
    int product = 1;
    for(int i=0;i<nums.size();i++){
        product = product * nums[i];
    }
    for(int i=0;i<nums.size();i++){
        ans[i]=(product/nums[i]);
    }
    for(int val : ans){
        cout<<val<<" ";
    }
}
int main(){
    vector<int> nums ={1,2,3,4};
    cout<<product(nums);
}