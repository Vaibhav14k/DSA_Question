#include<iostream>
using namespace std;
int decimal(int decimalnumber){
    int ans=0;int pow=1;
    while(decimalnumber>0){
        int reminder = decimalnumber % 2;
        decimalnumber/=2;
        ans= ans + (reminder*pow);
        pow = pow*10;
    }
    return ans;
}
int main(){
    cout<<decimal(50)<<endl;
    return 0;
}