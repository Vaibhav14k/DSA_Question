#include<iostream>
using namespace std;

void factoril(int n){
    int fact=1;
    for(int i=1;i<=n;i++){
        fact=fact*i;
    }
    cout<<fact<<endl;
}
int main(){
    factoril(3);
    return 0;
}