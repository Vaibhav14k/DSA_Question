#include<iostream>
#include<vector>
#include <unordered_map>
using namespace std;
vector<int> findAnagrams(string s, string p) {
        vector<int>result;
        unordered_map<char,int>count;
        for(char x:p){
            count[x]++;
        }
        int n=s.size();
        for(int st=0;st<n-p.size()+1;st++){
            for(int end=0;end<p.size();end++){

            }
        }
    }
int main(){
    string s="cbaebabacd";
    string p = "abc";
    // vector<int>findAnagrams(string s,string p);
    // cout<<s.size();
    vector<string>result;
    for(int i=0;i<=s.size()-3;i++){
        string sub="";
        unordered_map<char,int>frq;
        unordered_map<char,int>count;
        for(int j=i;j<i+3;j++){
            sub.push_back(s[j]);
            // count[s[j]]++;
        }
        for(char x:sub){
            frq[x]++;
        }
        for(char y:p){
            frq[y]--;
        }
        for(auto it : frq){
            if(it.second ==0){
                result.push_back(i);
            }
        }
        // result.push_back(sub);
    }
}