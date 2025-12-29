#include<iostream>
#include<vector>
using namespace std;
int binarysearch( vector<int>arr,int st,int end ,int target){
    int mid=st + (end-st)/2;
    if(arr[mid] == target){
        return mid;
    }
    else if(arr[mid]<target){
        return binarysearch(arr,mid+1,end,target);
    }else{
        return binarysearch(arr,st,mid-1,target);
    }
}
int main(){
    vector<int>arr = {-1,0,3,5,9,12};
    int target = 9;
    int st=0;
    int end=arr.size()-1;
    cout<<binarysearch(arr,st,end,target);
}