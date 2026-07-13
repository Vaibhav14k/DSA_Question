#include<iostream>
using namespace std;
void changevalue(int * ptr){
    *ptr = 20;
}
int main(){
    int a=10;
    changevalue(&a);
    cout<<"value of a is : "<<a<<endl;
}