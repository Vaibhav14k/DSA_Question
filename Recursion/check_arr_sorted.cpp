#include<iostream>
#include<vector>
using namespace std;


bool issorted(vector<int>arr,int n){
    if(n==0  || n==1 ){
        return n;
    }
    return arr[n-1]>=arr[n-2] && issorted(arr,n-1); 

}
int main(){
    vector<int> arr={1,2,3,4,5};
    int n=arr.size();
    cout<< issorted(arr,n);
    return 0;
}