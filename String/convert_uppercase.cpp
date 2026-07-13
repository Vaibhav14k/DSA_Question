#include<iostream>
using namespace std;
int main(){
    string s="vaibhav";
    for(char c: s){
        cout<<char(int(c)-32) ;
    }
    cout<<endl;
    string s1="VAIBHAV";
    for(char c1: s1){
        cout<<char(int(c1)+32) ;
    }
}
