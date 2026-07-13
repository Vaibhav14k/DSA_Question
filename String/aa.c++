#include<iostream>
#include<string>
using namespace std;
int main(){
    string s1="daabcbaabcbc";
    string part="abc";
    while (!s1.empty()){
        s1.erase(s1.find(part),(s1.find(part)+part.length()));
    }
}