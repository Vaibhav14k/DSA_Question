#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st(nums.begin(), nums.end());
        int longest = 0;
        for (int x : nums) {
            if (st.find(x - 1) == st.end()) {
                int current = x;
                int count = 1;
                while (st.find(current + 1) != st.end()) {
                    current++;
                    count++;
                }
                longest = max(longest, count);
            }
        }

        return longest;
};

int main() {
    int n;

    cout << "Enter the size of array: ";
    cin >> n;

    vector<int> nums(n);

    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    cout<<"longest "<<longestConsecutive<<endl;
    return 0;
}