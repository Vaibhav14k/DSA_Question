
#include<iostream>
#include<vector>
using namespace std; 
int main(){
    vector<int> arr= {1,1,1,2,4,5,6,7};
    int k =3;
    int maxlen=0;
    for(int i=0;i<arr.size();i++){
        for(int j=i;j<arr.size();j++){
            int sum =0;
            for(int k=i;k<=j;k++){
                cout<<arr[k];
                // sum += arr[k];
            }
            // if(sum ==k) maxlen = max(maxlen , j-i+1);
            cout<<endl;
        }
    }
    cout<<maxlen;
}