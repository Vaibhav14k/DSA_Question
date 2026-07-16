#include<iostream>
#include<vector>
using namespace std;
int  moveZeroes(vector<int>& nums) {
        int j=0;
        vector<int>temp;
        int count=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i] != 0){
                temp.push_back(nums[i]);
            }else{
                count++;
            }
        }
        for(int i=0;i<count;i++){
            temp.push_back(0);
        }
        for(int i=0;i<temp.size();i++){
            cout<<temp[i]<<" ";
        }
    }
int main(){
    vector<int> nums = { 1 , 0 ,1 , 2, 3,0,4,5,7,8,0,10};
    moveZeroes(nums);
}