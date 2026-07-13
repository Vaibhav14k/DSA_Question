#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> vec={1,2,3,4,5};
    // forawad iteration :   
    vector<int>::iterator it;
    for (it = vec.begin(); it != vec.end();it++ ){
        cout<<*(it)<<" "  <<endl;
    }
    // for reverse iteration : 
    for (auto it = vec.rbegin(); it != vec.rend();it++ ){
        cout<<*(it)<<" " ;
    }
}