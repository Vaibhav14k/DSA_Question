#include<iostream>
#include<string>
using namespace std;
int main(){
    string str;
    /// for input the string ; 
    cout<<"enter your strin";
    getline(cin,str);
    cout<<"output"<<str<<endl;

    // for the output the string : 
    for (char ch :str){
        cout<< ch << endl;
    }
}