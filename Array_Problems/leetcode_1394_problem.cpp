#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
int findLucky(vector<int>& arr) {

        unordered_map<int,int> mp;

        for(int x : arr)
            mp[x]++;

        int ans = -1;

        for(auto it : mp){
            if(it.first == it.second){
                ans = max(ans, it.first);
            }
        }

        return ans;
    }
int main(){
    vector<int > arr = {1,2,2,3,4,5,5,3};
    cout<<  "  lucky number :  " << findLucky(arr);
}