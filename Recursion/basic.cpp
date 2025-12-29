#include<iostream>
using namespace std;
void printnumber(int n){
    if (n == 1){
        cout<<"1\n";
        return ;
    }
    cout<<n <<" ";
    printnumber(n-1);

}
int main(){
    printnumber( 4);
    return 0;
}