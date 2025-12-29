#include<iostream>
using namespace std;
void changearr(int arr[],int size){
    cout<<"after t;he pass by value : ";
    for(int i=0;i<size;i++){
        arr[i]=arr[i]*2;
        cout<<arr[i]<<" ";
    }
}
int main(){
    int arr[]={1,2,3};
    changearr(arr,3);
    for(int i=0;i<3;i++){
        cout<<arr[i]<< " " ;
    }
}