#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        // Traverse from the last digit
        for (int i = digits.size() - 1; i >= 0; i--) {

            // If digit is less than 9, increment and return
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }

            // If digit is 9, make it 0 and continue
            digits[i] = 0;
        }

        // If all digits were 9, insert 1 at the beginning
        digits.insert(digits.begin(), 1);

        return digits;
    }
};

int main() {
    Solution obj;

    vector<int> digits = {9, 9, 9};

    vector<int> result = obj.plusOne(digits);

    cout << "Output: ";
    for (int num : result) {
        cout << num << " ";
    }

    return 0;
}