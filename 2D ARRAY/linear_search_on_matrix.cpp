#include<iostream>
using namespace std;
bool linearsearch(int matrix[4][3],int row,int coloum,int key){
    for (int i=0;i<row;i++){
        for(int j=0;j<coloum;j++){
            if(key==matrix[i][j]){
                return true;
            }
        }
    }
    return false;
}

int main(){
    int matrix[4][3]={{1,2,3},{4,5,6},{7,8,9}};
    int row=4;
    int coloum=3;
    cout<<linearsearch(matrix,row,coloum,20);
}