#include<iostream>
#include<vector>
using namespace std;

void merge(vector<int>& arr, int st, int mid, int end) {
    int i = st;
    int j = mid + 1;
    vector<int> temp;

    while (i <= mid && j <= end) {
        if (arr[i] < arr[j]) {
            temp.push_back(arr[i]);
            i++;
        } else {
            temp.push_back(arr[j]);
            j++;
        }
    }

    while (i <= mid) {
        temp.push_back(arr[i]);
        i++;
    }
    while (j <= end) {
        temp.push_back(arr[j]);
        j++;
    }

    // Copy sorted values back into arr
    for (int idx = 0; idx < temp.size(); idx++) {
        arr[st + idx] = temp[idx];
    }
}

void mergesort(vector<int>& arr, int st, int end) {
    if (st < end) {
        int mid = st + (end - st) / 2;

        mergesort(arr, st, mid);       // Left part
        mergesort(arr, mid + 1, end);  // Right part
        merge(arr, st, mid, end);      // Merge both
    }
}

int main() {
    vector<int> arr = {12, 31, 35, 8, 32, 17};
    int st = 0;
    int end = arr.size() - 1;
    // cout<<"size"<<arr.size();
    mergesort(arr, st, end);

    cout << "Sorted array: ";
    for (int x : arr) {
        cout << x << " ";
    }
}
