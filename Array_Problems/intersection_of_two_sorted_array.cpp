#include<iostream>
#include<vector>
using namespace std;
int intersection(vector<int> a , vector<int> b){
    int i=0;
    int j=0;
    int n1=a.size();
    int n2=b.size();
    vector<int>ans;
    while(i<n1 && j<n2){
        if(a[i] == b[j]  ){
            ans.push_back(a[i]);
            i++;
            j++;
        }
        else if(a[i]<b[j]){
            i++;
        }else{
            j++;
        }
    }
    for(auto it : ans){
        cout<<it<<" ";
    }
}
int main(){
    vector<int>  a = { 1,2,2,3,3,4,5,6};
    vector<int>b = { 2,3,3,5,6,6,7};
    intersection(a,b);
}