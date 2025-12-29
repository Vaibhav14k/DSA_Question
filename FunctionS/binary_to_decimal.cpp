#include<iostream>
using namespace std;

int binary(int binarynumber){
    int ans=0;
    int pow=1;
    while(binarynumber>0){
        int rem=binarynumber%10;
        ans = ans + (rem*pow);
        binarynumber = binarynumber/10;
        pow = pow*2;
    }
    return ans;
}

int main(){
    cout<<binary(10)<<endl;
    cout<<binary(101)<<endl;
}