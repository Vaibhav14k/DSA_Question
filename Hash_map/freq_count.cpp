#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    unordered_map<int,int>m;
    int arr[]={1,2,1,2,3,4};
    int n=6;
    for(int i=0;i<n;i++){
        m[arr[i]]++;
    }
    for(auto it:m){
        cout<<it.first<<" "<<it.second<<endl;
    }
}