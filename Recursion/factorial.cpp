#include<iostream>
using namespace std; 
int factoria(int n){
    if(n ==1){
        return n ;
    }
    return n*factoria(n-1);
}
int main(){
    cout<<factoria(4);
    return 0;
}