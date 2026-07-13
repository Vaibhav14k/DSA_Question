#include<iostream>
#include<unordered_map>
#include<unordered_set>
using namespace std;
bool ishappy(int n){
    unordered_set<int>s;
    while(n != 1){
        if(s.count(n)){
            return false;
        }
        int sum=0;
        s.insert(n);
        while(n>0){
            int digit = n%10;
            sum += digit * digit;
            n = n / 10;
        }
        n = sum;
    }
    return true;
};
int main(){
    int n=19;
    cout<<ishappy(n);
}