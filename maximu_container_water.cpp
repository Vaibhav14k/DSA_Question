#include<iostream>
#include<vector>
using namespace std;
int maxmumwater(vector<int>& height){
    int w ,h;
    int ans;
    int maxwater=0;
    for(int i=0;i<height.size();i++){
        for(int j=i+1;j<height.size();j++){
            w = j - i ;
            h = min(height[i],height[j]);
            ans = w * h;
            maxwater = max(maxwater,ans);
        }
    }
    return maxwater;
};
int main(){
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    cout<<maxmumwater(height);
}