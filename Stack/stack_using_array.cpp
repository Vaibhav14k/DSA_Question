#include<iostream>
#include<vector>
using namespace std;
class Stack{
    vector<int>v;
    public : 
    void push_back(int val){
        v.push_back(val);
    }
    void pop_back(){
        v.pop_back();
    }
    int top(){
        return v[v.size()-1];
    }
    bool empty(){
        return v.size() == 0;
    }
};
int main(){
    Stack s;
    s.push_back(10);
    s.push_back(20);
    s.push_back(30);
    while ( !s.empty()){
        cout<<s.top()<<" ";
        s.pop_back();
    }
}