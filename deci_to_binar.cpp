#include<iostream>
using namespace std; 
string tobinary(int n){
    string binary = "";
    if (n == 0) return "0";   // handle case when n=0

    while(n>0){
        binary = char('0'+(n%2)) + binary;
        n=n/2;
    }
    return binary;
}
int main(){
    int n=8;
    cout<<"binary : "<<tobinary(n);
}