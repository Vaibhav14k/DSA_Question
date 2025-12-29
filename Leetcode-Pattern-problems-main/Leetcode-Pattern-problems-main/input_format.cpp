#include <iostream>
#include <vector>

int main() {
    int t; // Number of test cases
    std::cin >> t;

    for(int i = 0; i < t; ++i) {
        int n; // Size of the array
        std::cin >> n;

        std::vector<int> arr(n);
        for(int j = 0; j < n; ++j) {
            std::cin >> arr[j];
        }

        // Process the array as needed
        for(int num : arr) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
