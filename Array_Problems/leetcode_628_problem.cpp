#include<iostream>
#include<vector>
using namespace std;
// finding the larest product of three number : and minimum element in the array is 3 
int main(){
    vector<int> nums = {-100,-98,-1,2,3,4};
    int n = nums.size();
    int product1  = nums[n-1] * nums[n-2] * nums[n-3];
    int product2 = nums[0] * nums[1] *  nums[n-1];
    cout<<max(product1 , product2);
}