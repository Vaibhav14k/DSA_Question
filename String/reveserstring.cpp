#include<iostream>
#include<string>

using namespace std ;
int main(){
    string str1="deva";
    int st=0;
    int end=str1.length()-1;
    while (st<=end)
    {
        swap(str1[st],str1[end]);
        st++ ;
        end --;
    }
    cout<<str1<<endl;
}