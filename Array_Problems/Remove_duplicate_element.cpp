#include<iostream>
#include<vector>
using namespace std;
int  removeduplicate (vector<int>arr){
    int i=0;
    for(int j=1;j<arr.size();j++){
        if(arr[i] != arr[j]){
            arr[i+1] = arr[j];
            i++;
        }
    }
    return i+1 ;
}
int main(){
    vector<int>arr = { 1, 1, 2 , 3, 4 , 5, 5};
    cout<<"size of array after remove duplicate " <<removeduplicate(arr);
}