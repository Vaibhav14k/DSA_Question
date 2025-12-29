#include<iostream>
#include<stack>
using namespace std;
int main(){
    stack <int> s;
    s.push(3);
    s.push(3);
    s.push(1);
    // for ( int val : s){
    //     cout<<val << " ";
    // }
    while (!s.empty()){
        cout<<s.top()<< " ";
        s.pop();
    } 
}