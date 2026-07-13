#include<queue>
#include<iostream>
using namespace std;
int main(){
    deque<int> d= {2,1,3,4,5,6,6};
    // l.push_back(2);
    // l.push_front(1);
    // l.push_back(3);
    // l.push_front(2);
    for (int val : d){
        cout<<val<<" " ;
    }
}