#include<iostream>
using namespace std;
void reverserarr(int arr[],int size){
    int start = 0;
    int end=size-1;
    while ( start <= end)
    {
        swap(arr[start],arr[end]);
        start = start + 1;
        end=end-1;
        cout<<endl;
    }
    
}   
int main(){
    int arr[]={1,2,3,4,5};
    reverserarr(arr,5);
    for(int i=0;i<5;i++){
        cout<<arr[i];
    }
}

// cout<<(arr[i]=arr[size-1]);
//         cout<<(arr[i+1]=arr[size-2]);
//         cout<<(arr[i+2]=arr[size-3]);
//         cout<<(arr[i+3]=arr[size-4]);
//         cout<<(arr[i+4]=arr[size-5]);
//         cout<<endl;