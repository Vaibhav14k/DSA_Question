#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    vector<int> arr = {1,2,3, 4, 5};
        int n= arr.size();
    // vector<int>ans(n);
    // for(int i=0;i<n;i++){
    //     ans[i] = arr[n-i-1];
    // }
    // for(int i=0;i<ans.size();i++){
    //     cout<<ans[i]<<endl;
    // }
    int left = 0;
    int right = n-1;
    while(left < right){
        swap(arr[left],arr[right]);
        left ++ ;
        right --;
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<endl;
    }
}