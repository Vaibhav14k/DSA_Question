#include<iostream>
#include<string>
using namespace  std;
bool ispalindrom(string x){
    string st2=x;
    int st=0;
    int end=x.length()-1;
    while (st<end)
    {
        swap(st2[st],st2[end]);
        st++;
        end--;
    }
    return st2==x;
    
}
int main(){
    string x="madma";
    ispalindrom(x);
}