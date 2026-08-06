#include<iostream>
using namespace std;
int smallestNumber(int n, int t){
    while(true){
        int ori = n;
        int prodcut =1 ;
        while(ori > 0){
            prodcut  *= (ori % 10);
            ori /= 10;
        }
        if(prodcut% t ==0){
            return n;
        }
        n++;
    }
}
int main(){
    int n, t;

    cout << "Enter n: ";
    cin >> n;

    cout << "Enter t: ";
    cin >> t;

    int ans = smallestNumber(n, t);

    cout << "Smallest Number = " << ans << endl;

    return 0;
}