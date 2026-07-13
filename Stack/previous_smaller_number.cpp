#include<iostream>
#include<stack>
#include<vector>
using namespace std;
int main(){
    stack<int>s;
    vector<int>  arr = { 6,8,0,1,3};
    vector<int> ans(arr.size(),0);
    for(int i=0;i<arr.size();i++){
        while(s.size()>0 && s.top() >= arr[i] ){
            s.pop();
        }
        if( s.size() ==0   ){
            ans[i]=-1;
        }
        else{
            ans[i]= s.top();
        }
        s.push(arr[i]);
    }
    for(int val : ans){
        cout<<val<<" ";
    }
    return 0;
}