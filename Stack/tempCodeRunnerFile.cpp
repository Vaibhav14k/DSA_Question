#include<iostream>
#include<vector>
#include<stack>
using namespace std;
int main(){
    vector<int>value={6,8, 0,1,3};
    vector<int>ans(value.size(),0);
    stack<int>s;
    for(int i=value.size();i>0;i--){
        while ( s.size()>0 && s.top()<=value[i] ){
            s.pop();
        }
        if(s.empty()){
            ans[i] = -1;
        }
        else {
            ans[i] = s.top();
        }
    }
}
