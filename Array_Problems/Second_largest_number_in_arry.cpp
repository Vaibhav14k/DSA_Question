#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> arr = {3, 4, 5,2,1 };
    int largest = arr[0];
    for(int i=1;i<arr.size();i++){
        if(arr[i]>largest){
            largest = arr[i];
        }
    }
    cout<<" largest number is : "<< largest <<endl ;
    cout<<"Hello" ;
}