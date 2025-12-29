#include<iostream>
#include<set>
#include<unordered_set>
using namespace std;
int main(){
    unordered_set<string , int>m;
    

    m.erase("tv");
    for (auto p:m){
        cout<<p.first<<" "<<p.second<<endl;
    }
}