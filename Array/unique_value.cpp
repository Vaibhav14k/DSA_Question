#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int>vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(4);
    int ans=0;
    for (int element:vec){
        ans = element^ans;
    }
     cout<<ans<<endl;
}