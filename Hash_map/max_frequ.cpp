#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    unordered_map<int,int>m;
    int arr[]={1,2,1,2,3,4,5,5,6,6,6};
    int n=11;
    int maxfreq=0;
    int element;
    for(int i=0;i<n;i++){
        m[arr[i]]++;
    }
    for(auto it:m){
        if(it.second>maxfreq){
            maxfreq=it.second;
            element=it.first;
        }
    }
    cout<<element<<" "<<maxfreq<<endl;
}