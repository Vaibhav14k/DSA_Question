#include<iostream>
using namespace std;
int sumofnumber(int n){
    if(n==1){
        return 1;
    }
    return (n+sumofnumber(n-1));
}
int print(int n){
    if(n==0) return n;
    cout<<n<<" ";
    return print(n-1);
}
int sum(int n){
    if(n==1) return n;
    return n + sum(n-1);
}
int fact(int n){
    if(n==1){
        return n;
    }
    return n*fact(n-1);
}
int fib(int n){
    if(n==0 ||  n==1 ){
        return n;
    }
    return fib(n-1) + fib(n-2);
}
int main(){
    // cout  << sumofnumber(5);
    // cout<<print(5);
    // cout<<sum(5);
    cout<<fact(4);
    cout<<fib(5);
    return 0 ;
}

