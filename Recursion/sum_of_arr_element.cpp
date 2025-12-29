#include<iostream>
#include<vector>
using namespace std;
int sumarr(vector<int>&arr,int n)
{
    if(n==0){
        return n;
    }
    return arr[n] + sumarr(arr,n-1);

}
int main(){
    vector<int>arr = {1,2,3,4,5};
    int n=arr.size()-1;
    cout<<sumarr(arr,n);
}