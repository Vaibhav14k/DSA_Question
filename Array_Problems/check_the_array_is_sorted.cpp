#include<iostream>
#include<vector>
using namespace std;
int checkthearray(vector<int> arr ){
    for(int i=1;i<arr.size();i++){
        if(arr[i-1]<arr[i]){
        }else{
            cout<<"return false";
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> arr = {1,2,3,4,5};
    cout<<checkthearray(arr);
}