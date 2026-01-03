#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    unordered_map<int,int>m;
    m[1]=100;
    m[2]=100;
    m[2]=300;
    m[3]=400;
    m[0]=100;
    for(auto it:m){
        cout<<it.first<<" "<<it.second<<endl;
    }
    m.erase(2);
    cout<<"new map"<<endl;
    for(auto it:m){
        cout<<it.first<<" "<<it.second<<endl;
    }
}