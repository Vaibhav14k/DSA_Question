#include<iostream>
using namespace std;
int swaping(int nums[],int n){
    int low=0;
    int mid=0;
    int high=n-1;
    while (mid <= high){
            if ( nums[mid] == 0 ){
                swap(nums[mid],nums[low]);
                mid++;
                low++;
            }
            else if ( nums[mid] == 1 ){
                mid++;
            }
            else {
                swap(nums[high],nums[mid]);
                high--;
            }
    }
}
int printarray(int num[],int n){
    for (int i=0;i<n;i++){
        cout<<num[i]<<" ";
    }
}
int main(){
    int num[]={2,0,2,1,1,0};
    int n=6;
    swaping( num, n);   
    printarray(num,n);

}