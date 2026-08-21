#include<iostream>
#include<vector>
using namespace std;

int main(){
    int r , c;
    cout<<"enter the row"<<endl;
    cin>>r;
    cout<<"enter the coloum "<<endl;
    cin>>c;
    int arr[r][c];
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<"enter the row "<< i << "enter the coloum "<< j <<endl; 
            cin>>arr[i][j];
        }
    }
    cout<<"final array "<<endl;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }

}