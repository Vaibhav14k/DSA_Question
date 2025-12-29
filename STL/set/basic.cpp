#include<iostream>
#include<set>
#include<vector>
using namespace std;
int main(){
    vector<int> nums={3,2,2,1};
    set<int>m(nums.begin(),nums.end());
    for (auto val : m){
        cout<<val<<endl;
    }
}