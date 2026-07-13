#include<iostream>
#include<set>

using namespace std;
int main(){
    multiset<int>m;
    m.insert(1);
    m.insert(2);
    m.insert(3);
    m.insert(4);
    m.insert(5);    m.insert(3);
    m.insert(4);
    m.insert(5);

    for (auto val : m){
        cout<<val<<endl;
    }
}