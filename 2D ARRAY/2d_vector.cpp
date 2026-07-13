#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<vector<int>> vec_matr={{1,2,3},{4,5,6},{7,8,9}};
    for(int i=0;i<vec_matr.size();i++){
        for (  int j=0; j<vec_matr[i].size();j++ ){
            cout<<vec_matr[i][j]<<endl;
        }
    }
}