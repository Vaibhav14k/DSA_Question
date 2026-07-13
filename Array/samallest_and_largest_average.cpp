#include<iostream>
using namespace std;

int main(){
    int arr[] ={1,9,8,3,10,5};
    int min=INT8_MAX;
    int max=INT8_MIN;
    for (int i=0;i<6;i++){
        if (min>arr[i]){
            min = arr[i];
        }
        if (max<arr[i]){
            max = arr[i];
        }
    }
    cout<<min<<endl;
    cout<<max<<endl;
    cout<<float(min+max)/2<<endl;
}