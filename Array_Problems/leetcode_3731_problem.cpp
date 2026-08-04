#include<iostream>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    vector<int>arr = {1,2,4,5};
    vector<int>result;
    sort(arr.begin(),arr.end());
    unordered_set<int> st(arr.begin(),arr.end());
    int min = arr[0];
    int max= arr[arr.size()-1];
    for(int i=min ; i<max;i++){
        if(st.find(i) == st.end()){
            result.push_back(i);
        }
    }
    for(int x : result){
        cout<<"misngin number "<<x<<endl;
    }
}