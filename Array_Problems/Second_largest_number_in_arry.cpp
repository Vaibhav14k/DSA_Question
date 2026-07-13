#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> arr = {3, 4, 5,2,1 };
    int largest = arr[0];
    int second = -1 ;
    for(int i=1;i<arr.size();i++){
        if(arr[i]>largest){
            second = largest;
            largest = arr[i];
        }
        else if (  arr[i]<largest && arr[i] > second){
            second = largest ; 
        }
    }
    cout<<" second largest number : "<<second <<endl;
}