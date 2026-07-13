
#include<iostream>

#include<vector>
using  namespace std;

void merge(vector<int>&arr, int st, int mid,int end   ){
    vector<int> temp;
    int i=st;
    int j=mid+1;
    //left 
    while(  i<=mid && j<= end  ){
        if ( arr[i] <= arr[j]  ){
            temp.push_back(arr[i]);
            i++;
        }
        else {
            temp.push_back(arr[j]);
            j++;
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


}


void mergesort(vector<int>&arr,int st,int end){
    if(st<end){
        int mid= st + (end-st)/2;
        //left :
        mergesort(arr,st,mid);
        //right : 
        mergesort(arr,mid+1,end);

        // merege sort array : 
        merge(arr,st,mid,end);
    }
}
int main(){
    vector<int> arr={12,31,35,8,32,17};
    int st=0;
    int end = arr.size()-1;
    mergesort(arr,st,end);
    for(int val : arr){
        cout<<val<<" " ;
    }
    cout<<endl;
    return 0;

}