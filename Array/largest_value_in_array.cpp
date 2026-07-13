#include<iostream>
#include<climits>
using namespace std;
int main(){
    int largest=INT8_MAX;
    int a= INT8_MIN;
    int arr[5]={45,300,44,22,1};
    for(int i=0;i<5;i++){
        if(arr[i]>largest){
            largest=arr[i];
        }
    }
    cout<<"largest value is "<<largest<<endl;
}