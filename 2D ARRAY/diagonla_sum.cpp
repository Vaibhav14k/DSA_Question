#include<iostream>
using namespace std;
int diagoalsum(int matrix[][3],int row,int colo,int n){
    int sum=0;
    for (int i=0;i<row;i++){
        for (int j=0;j<colo;j++){
            if(i == j){
                sum += matrix[i][j];
            }
            else if ( j ==n-i-1   ){
                    sum+=matrix[i][j];
            }
        }
    }
    return sum;
}
int main(){
    int matrix[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    int row=3;
    int colo=3;
    int n=3;
    cout<<diagoalsum(matrix,row,colo,n);
    
    return 0;
}