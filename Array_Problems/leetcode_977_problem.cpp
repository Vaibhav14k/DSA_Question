#include<iostream>
#include<vector>
#include<algorithm>
// #include<sor
using namespace std;
int main(){ 
    vector<int>  num = {-7,-2,0,1,5,6};
    for(int i=0;i<num.size();i++){
        num[i] = num[i] * num[i];
    }
    sort(num.begin(),num.end());
    for(int x : num){
        cout<< x << endl;
    }

}