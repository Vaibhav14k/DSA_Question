#include<iostream>
#include<string>
using namespace std;
int main(){
    string str="vaibhav kangnae";
    string str1="abc";
    cout<<str1.length();
    string str2 = str + str1;
    cout<<str2<<endl;
    // cout<<str<<endl;

    string strr1="vaibhav";
    string STRR2="vaibhav";
    cout<< (strr1 == STRR2);

    string hey;
    getline(cin,hey);
    cout<<"output"<<hey<<endl;
}