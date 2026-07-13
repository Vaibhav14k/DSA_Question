#include<iostream>
#include<vector>
using namespace std;
int binarySerach(vector<int>arr1,int target){
    int st = 0 ; 
    int end = arr1.size()-1;
    while (st<=end)
    {   
         int mid = (st + end)/2;
        if (target == arr1[mid] ){
            cout<<"target is found at "<< mid <<endl;
            return mid;
        }
        else if(target > arr1[mid]){
            st = mid + 1;
        }
        else {
            end = mid-1;
        }
    }
    return -1;
}
int main(){
    vector<int>arr1 = {1,2,3,22,44,55,77};
    int target =44;
    cout<<binarySerach(arr1,target)<<endl;
}