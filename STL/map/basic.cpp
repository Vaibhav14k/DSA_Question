#include<iostream>
#include<map>
using namespace std;
int main(){
    map<int,string>m;
    // map<string,int>m1;
    m[1]="abc";
    m[2]="bcd";
    m[3]="sd";
    m.insert({4,"xya"});
    for(auto p:m){
        cout<<p.first<<" "<<p.second<<endl;
    }
}