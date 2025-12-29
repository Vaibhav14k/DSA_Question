#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>vec;
    vec.push_back(20);
    vec.push_back(10);
    vec.push_back(30);
    vec.push_back(30);
    cout<<vec.capacity();
    vec.push_back(10);
    cout<<endl;
    cout<<vec.capacity();
}