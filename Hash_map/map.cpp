#include<iostream>
#include<map>
using namespace std;
int main(){
    map<int,int>m;
    m[1]=100;
    m[3]=100;
    m[2]=100;
    m[4]=40;
    m[4]=50;
    for(auto it:m){
        cout<<it.first<<" "<<it.second<<endl;
    }
}