#include<iostream>
#include<vector>
using namespace std;
vector<int> unionarray ( vector<int > arr1 , vector<int> arr2){
    int n1 = arr1.size();
    int n2 = arr2.size();
    vector<int> unionarr;
    int i=0;
    int j=0;
    while(i<n1 && j<n2){
        if(arr1[i] <= arr2[j]){
            if( unionarr.size() == 0 ||    unionarr.back() != arr1[i]){
                unionarr.push_back(arr1[i]);
            }
            i++;
        }
        else{
            if(unionarr.size() == 0 || unionarr.back() != arr2[j] ){
                unionarr.push_back(arr2[j]);
            }
            j++;
        }
    }
    while(j<n2){
        if(unionarr.size() == 0  || unionarr.back() != arr2[j] ){
            unionarr.push_back(arr2[j]);
        }
        j++;
    }
    while(i<n1){
        if( unionarr.size() == 0 ||    unionarr.back() != arr1[i]){
                unionarr.push_back(arr1[i]);
            }
            i++;
    }
    return unionarr;
}
int main(){
    vector<int> arr1 = { 1, 1, 2 , 3, 4, 5};
    vector<int> arr2 = { 1, 1, 2 , 3, 4, 5};
    unionarray(arr1,arr2);
}