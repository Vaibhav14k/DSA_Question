#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    string a="aaabbbccd";
    unordered_map<char,int>result;
    for(char ch : a){
        result[ch]++;
    }
    int count=0;
    for(auto ch: result){
        // cout<<ch.first<<" "<<ch.second<<endl;
        if(ch.second == 2){
            count++;
        }
    }
    // return count;
    cout<<count;
}