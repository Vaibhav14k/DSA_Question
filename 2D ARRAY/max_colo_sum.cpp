#include<iostream>
#include<climits>
using namespace std;
int maxclooumsum(int matrix[][3],int row,int col){
    int coloumsum=INT_MIN;
    for(int i=0;i<row;i++){
        int sum=0;
        for(int j=0;j<col;j++){
            sum += matrix[j][i];
        }
        coloumsum=max(coloumsum,sum);
    }
    return coloumsum;
}
int main(){
    int matrix[3][3]={{1,2,3},{3,45,6},{7,8,9}};
    int row=4;
    int col=3;
    cout<<maxclooumsum(matrix,row,col);
    return 0;
}