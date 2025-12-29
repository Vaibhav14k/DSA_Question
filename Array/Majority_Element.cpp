#include<iostream>
#include<climits>
using namespace std;
int main(){
    int n=4;
    int repeat;
    int fre;
    int arr[]={2,2,1,2,2};
    for (int i=0;i<n;i++){
             fre=0;
            for( int j=0;j<n;j++){
                if (arr[i]==arr[j]){
                    repeat=arr[i];
                    
                    fre ++;
                }
            }
    }
    if (fre> n/2){
        cout<<"most repeat number is : "<<repeat;
    }
}