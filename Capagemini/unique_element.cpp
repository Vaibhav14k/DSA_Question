#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
int main(){
    vector<int> nums = {2,2,1,2,4,2,5,6,5,7};
    unordered_map<int,int>result;
    for(int x:nums){
        result[x]++;
    }
    int count=0;
    for(auto y : result   ){
        cout<<y.first<<" "<<y.second<<endl;
        if(y.second<2){
            count++;
        }
    }
    // cout<<count;
}