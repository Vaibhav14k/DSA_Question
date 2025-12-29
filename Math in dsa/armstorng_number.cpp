#include<iostream>
#include<math.h>
using namespace std;
bool isaramstorng(int n){
    int copynumber=n;
    int sumofcube=0;
    while (n != 0)
    {
        int digit = n % 10;
        sumofcube += (digit* digit*digit);
        n = n / 10 ;
    }
    return sumofcube == copynumber;
    
}
int main(){
    int n = 13;
    if ( isaramstorng(n)){
        cout<<" it is an armastrong number : ";
    }
    else{
        cout<<" not an aramstrong number : ";
    }
}