#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> vectorname;
    vectorname.push_back(2);
    vectorname.push_back(2);
    vectorname.push_back(2);
    vectorname.push_back(2);
    vectorname.push_back(3);
    cout<<vectorname.size()<<endl;
    cout<<vectorname.capacity();
    // for (int val: vectorname){
    //     cout<<val<<" ";
    // }
    cout<<" " <<  *(vectorname.begin());
    cout<<" " <<  *(vectorname.end());


}
