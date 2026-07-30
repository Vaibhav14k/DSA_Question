#include<iostream>
#include<vector>
#include<map>
#include<unordered_map>
using namespace std;
int majority(vector<int> nums){
    unordered_map<int,int>mp;
    for(int i=0;i<nums.size();i++){
        mp[nums[i]]++;
    }
    int num;
    int maxx=-1;
    for(auto val : mp){
        if( val.second >maxx){
            num = val.first;
            maxx = val.second;
        }
    }
    return num;
}
int main(){
    vector<int> num = {2,2,1,3,1,2,2,3,2,2,};
    cout<<majority(num);
}