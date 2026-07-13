#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;
bool isiosmorphich(string s1,string s2){
    unordered_map<char,string>mp1;
    unordered_map<string,char>mp2;
    vector<string>words;
    string temp=" ";
    for(char c:s2){
        if(c != ' '){
            temp += c;
        }else{
            words.push_back(temp);
            words.push_back(temp);
            temp= " ";
        }
    }
    words.push_back(temp);
    for(int i=0;i<s2.length();i++){
        unordered_map<char,string>mp1;
        unordered_map<string,char>mp2;
        char p = s1[i];
        string w= words[i];
        if(mp1.count(p) && mp1[p]!=w ) return false;
        if(mp2.count(w) && mp2[w]!=p ) return false;
        mp1[p]=w;
        mp2[w]=p;
    }
    return true;
};
int main(){
    string s1 = "abab";
    string s2 = "dog cat dog cat";
    cout<<isiosmorphich(s1,s2); 
}