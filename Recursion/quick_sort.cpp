#include<iostream>
#include<vector>
using namespace std;

int partion(vector<int> & arr, int start, int end){
    int idx = start - 1;
    int pivet = arr[end];
    for(int j=start;j<end;j++){
        // for decesding make it in arr[j] >= pivet : 
        if (  arr[j] <= pivet  ){
            idx++;
            swap(arr[j],arr[idx]);
        }
    }
    idx++;
    swap(arr[end],arr[idx]);
    return idx;
}


void quicksort(vector<int> & arr, int start, int end ){
    if(start<end){
        int pivotidx = partion(arr,start,end);
        // left : 
        quicksort(arr,start,pivotidx-1);
        //right : 
        quicksort(arr,pivotidx+1,end);
    }
}



int main(){
    vector<int> arr={5,2,6,4,1,3};
    quicksort(arr,0,arr.size()-1);
    for(int val :  arr  ){
        cout<<val<<" ";
    }
    cout<<endl;
    return 0;
}