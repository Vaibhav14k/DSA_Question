#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;
bool canConstruct(string s1, string s2) {
        unordered_map<char,int>m;
        for(char c:s2){
            m[c]++;
        }
        for(char c:s1){
            if(m.find(c) ==m.end() || m[c]>0  ){
                return false;
            }
            m[c]--;
        }
        return true;
    }
int main(){
    string s1="a";
    string s2="ab";    
    cout<<canConstruct(s1,s2);
}