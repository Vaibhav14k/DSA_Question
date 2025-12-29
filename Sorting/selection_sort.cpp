#include<iostream>
using namespace std;
int selection_sort(int arr[],int n){
    for (int i=0;i<n-1;i++){
        int min = i;
        for (int j=i+1;j<n;j++){
            if ( arr[min] > arr[j] ){
                min = j;
            }
        }
        if (min != i){
            swap(arr[i],arr[min]); 
        }
    }
}
int printarray(int arr[],int n){
    for ( int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
int main(){
    int arr[]={7,4,10,6,3,1} ;
    int n = 6;
    selection_sort(arr,n);
    printarray(arr,n);
}