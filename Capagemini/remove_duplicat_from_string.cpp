#include<iostream>
#include<unordered_map>
#include<queue>
using namespace std;
int main(){
    string s="hellotto";
    unordered_map<char,bool> arr;
    queue<int>q;
    string result;
    for(int i=0;i<s.size();i++){
        if(!arr[s[i]]){
            q.push(s[i]);
            arr[s[i]] = true;
        }
    }
    while(q.size()>0){
        result += q.front();
        q.pop();
    }
    cout<<result;
}