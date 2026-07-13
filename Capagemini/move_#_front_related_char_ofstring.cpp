#include<iostream>
#include<vector>
using namespace std;
int main(){
    string s="vaibha##v";
    int count=0;
    string result="";
    for(int i=0;i<s.size();i++){
        if(s[i]=='#'){
            count++;
        }else{
            result += s[i];
        }
    }
    for(int i=0;i<count;i++){
        result = '#'+result;
    }
    cout<<result<<endl;
} 