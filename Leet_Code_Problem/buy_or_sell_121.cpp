#include <iostream>
#include <vector>

using namespace std;

bool isSpecialArray(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; i++) {
        // Check if both numbers have the same parity (both even or both odd)
        if ((nums[i] % 2) == (nums[i + 1] % 2)) {
            return false;
        }
    }
    return true; // If all adjacent pairs have different parity
}

int main() {
    vector<int> nums1 = {4, 3, 1, 6};
    vector<int> nums2 = {1, 2, 3, 4, 5, 6};
    vector<int> nums3 = {2, 4, 6, 8};

    cout << boolalpha;  // Print `true` or `false` instead of 1 or 0
    cout << "Result for nums1: " << isSpecialArray(nums1) << endl; // false
    cout << "Result for nums2: " << isSpecialArray(nums2) << endl; // true
    cout << "Result for nums3: " << isSpecialArray(nums3) << endl; // false

    return 0;
}
