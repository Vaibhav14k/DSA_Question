#include<iostream>
using namespace std;
#include<math.h>
int printdigit(int n){
    int sum =0;
    while( n!= 0 ){
        int digit = n % 10;
        sum = sum + digit;
        n = n/10;
    }
    return sum;
}

int main(){
    int n=43211;
    cout<<printdigit(n);
    return 0;
}