#include<iostream>
#include<vector>
using namespace std; 
int main(){
    int  x = 121;
    int original = x;
    int revere=0;
    while(x>0){
        int digit = x % 10;
        revere = revere * 10 + digit;
        x = x/10;
    }
    if(revere == original){
        cout<<"plindrome number ";
    }else{
        cout<<"not palindrome numbe";
    }
}