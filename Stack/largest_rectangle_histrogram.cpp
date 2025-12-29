#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> right(n, n);  // index of next smaller to right
        vector<int> left(n, -1);  // index of previous smaller to left
        stack<int> s;

        // Fill right
        for (int i = n - 1; i >= 0; i--) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            if (!s.empty()) {
                right[i] = s.top();
            }
            s.push(i);
        }

        // Clear the stack for left processing
        while (!s.empty()) s.pop();

        // Fill left
        for (int i = 0; i < n; i++) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            if (!s.empty()) {
                left[i] = s.top();
            }
            s.push(i);
        }

        // Calculate max area
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int width = right[i] - left[i] - 1;
            int currentArea = heights[i] * width;
            cout<<currentArea<<endl;
        }
    }
};

int main() {
    Solution sol;

    // Example input
    vector<int> heights = {2, 1, 5, 6, 2, 3};

    // Compute and print result
    int result = sol.largestRectangleArea(heights);
    // cout << "Largest Rectangle Area: " << result << endl;

    return 0;
}
