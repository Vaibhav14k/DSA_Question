#include<iostream>
#include<list>
using namespace std;
int main(){
    list<int> l={2,1,3,4,5,6,6};
    // l.push_back(2);
    // l.push_front(1);
    // l.push_back(3);
    // l.push_front(2);
    for (int val : l){
        cout<<val<<" " ;
    }
}