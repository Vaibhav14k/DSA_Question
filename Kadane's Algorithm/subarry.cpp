#include<iostream>
using namespace std;
int main(){
    int n = 5;
    int maxx=0;
    int arr[5] = {1,2,3,4,5};
    for(int st =0; st<n;st++){
        int sum=0;
        for(int end=st;end<n;end++){
                sum += arr[end];
                maxx= max(sum,maxx);
            
            // cout<<" ";
        }
        cout<<endl;
    }
    cout<<maxx;
}