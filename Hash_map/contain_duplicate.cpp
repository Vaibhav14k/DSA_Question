#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;
bool containcheck(vector<int>&nums){
    unordered_map<int,int>m;
    for(int i=0;i<nums.size();i++){
        m[nums[i]]++;
    }
    for(auto x:m){
        if(x.second>1){
            return true;
        }
    }
    return false;
};
int main(){
    vector<int>nums = {1,1,2,3,4,5};
    cout<<containcheck(nums);
}