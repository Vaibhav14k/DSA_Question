#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int>vecc;
    int n;
    cout<<"enter the number of element : ";
    cin>>n;
    for (int i=0;i<n;i++){
        int val;
        cout<<"enter the value : ";
        cin>>val;
        vecc.push_back(val);
    }
    for (int element : vecc){
        cout<<element<<endl;
    }
}