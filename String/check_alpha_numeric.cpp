#include<iostream>
using namespace std;

int main(){
    string s="vaibhav";
    int st=0;
    int end=s.length()-1;
    while (st<end)
    {
        if(   (s[st]>='0' && s[st] <='9')  || (  tolower(s[st]) >='a' && tolower(s[end]) <='z')){
            cout<<"it's an aplh numeric";
            break;
        }
        st++; 
        end--;
        }
    cout<<"it'is not alph numeric     ";
}