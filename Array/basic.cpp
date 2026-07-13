#include<iostream>
using namespace std;
int main(){
    // int marks[4]={1,2,3,4};
    // cout<<marks[0]<<endl;
    // cout<<marks[1]<<endl;
    // cout<<marks[2]<<endl;
    // cout<<marks[3]<<endl;

    int marks[4];
    for(int i=0;i<4;i++){
        cout<<"enter the value of array : ";
        cin>>marks[i];
        cout<<"valaue of arrya at "<< i << endl;
        cout<<marks[i]<<endl;
    }
}