#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max1 = INT_MIN;
        int max2 = INT_MIN;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];

            if (num > max1) {
                max2 = max1;
                max1 = num;
            } 
            else if (num > max2) {
                max2 = num;
            }
        }

        return (max1 - 1) * (max2 - 1);
    }
};

int main() {

    vector<int> nums = {3, 4, 5, 2};

    Solution obj;

    int result = obj.maxProduct(nums);

    cout << "Maximum Product: " << result << endl;

    return 0;
}