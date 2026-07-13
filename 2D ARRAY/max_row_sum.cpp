#include<iostream>
#include<climits>
using namespace std;
int maxrowsum(int matrix[][3],int row,int col){
    int rowsum=INT_MIN;
    for(int i=0;i<row;i++){
        int sum=0;
        for(int j=0;j<col;j++){
            sum += matrix[j][i];
        }
        rowsum=max(rowsum,sum);
    }
    return rowsum;
}
int main(){
    int matrix[4][3]={{1,2,3},{3,5,6},{7,8,9},{1,2,3}};
    int row=4;
    int col=3;
    cout<<maxrowsum(matrix,row,col);
    return 0;
}