#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
int main(){
    vector<int> arr  = {1,1,2,3,3,4,4,5,5};
    unordered_map<int,int>mp;
    for(int i=0;i<arr.size();i++){
        mp[arr[i]]++;
    }
    for(auto it :mp){
        if(it.second == 1){
            cout<<"single oocurs : "<<it.first;
        }
    }
}