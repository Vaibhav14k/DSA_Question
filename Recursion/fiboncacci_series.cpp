#include<iostream>
using namespace std;
void fibonacci_series(int n){
    int a=0,b=1;
    for (int i=2;i<n;i++){
        int c= a+b;
        a=b;
        b=c;
        cout<< c << " " <<endl;
    }
}
int main(){
    fibonacci_series(10);
}