#include<iostream>
using namespace std;
int main(){
    int matrix[2][3];
    int row=2;
    int coloum=3;
    cout<<"input matrix"<<endl;
    for(int i=0;i<row;i++){
        for(int j=0;j<coloum;j++){
            cin>>matrix[i][j];
        }
    }
    cout<<"output matrix"<<endl;
    for(int i=0;i<row;i++){
        for(int j=0;j<coloum;j++){
            cout<<matrix[i][j];
        }
        cout<<endl;
    }
}