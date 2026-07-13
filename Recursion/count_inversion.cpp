#include<iostream>
#include<vector>
using namespace std ;
int merge(vector<int>& arr, int st, int mid , int end){
    int i=st ,j=mid+1;
    int invcount =0;
    vector<int> temp;
    while( i<= mid && j<=end){
        if(arr[i]<= arr[j]){
            temp.push_back(arr[i]);
            i++;
        }
        else {
            temp.push_back(arr[j]);
            j++;
            invcount+= (mid -i +1)  ;
        }
    }
    while(i<=mid){
            temp.push_back(arr[i]);
            i++;
    }
    while(j<=end){
        temp.push_back(arr[j]);
        j++;
    }
    for(int idx=0;idx<temp.size();idx++){
        arr[idx+st]=temp[idx];
    }
    return invcount ;
}


int mergesort(vector<int> & arr,int st , int end   ){
    if(st<  end){
        int mid = st + (end - st)/2 ;
        int leftcount = mergesort(arr,st,mid); 
        int rightcoutn = mergesort(arr,mid+1,end);
        int invercount= merge(arr,st,mid,end);
        return leftcount+rightcoutn+invercount;
    }      
}

int main(){
    vector<int> arr =  {6,3,5,12,7,1};
    int ans = mergesort(arr,0,arr.size()-1);
    cout<<"count inversion : " << ans ;
    return 0;
}