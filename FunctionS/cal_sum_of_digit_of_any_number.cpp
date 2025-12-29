#include<iostream>
using namespace std;
// int main(){
//     int num=145;
//     int num1=num%10;
//     cout<<num1<<endl;
//     cout<< (num/10)<<endl;
//     num=14;
//     int num2=num%10;
//     num=1;
//     int num3=num%10;
//     cout<<(num1+num2+num3)<<endl;
// }
int main(){
    int num=145;
    int x=0;
    for(int i=1;i<=3;i++){
        x=x+num%10;
        // cout<<x<<endl;
        int num1 = num/10;
        cout<<num1<<endl;
    }
    // cout<<x<<endl;
    
}