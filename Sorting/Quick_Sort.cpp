#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int st, int end) {
    int pivot = arr[end];
    int i = st - 1;

    for(int j = st; j < end; j++) {
        if(arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i+1], arr[end]);
    return i + 1;
}


void quicksort(vector<int>& arr, int st, int end) {
    if(st < end) {
        int pivotIdx = partition(arr, st, end);
        quicksort(arr, st, pivotIdx - 1);
        quicksort(arr, pivotIdx + 1, end);
    }
}

int main() {
    vector<int> arr = {12, 31, 35, 8, 32, 17};
    int st = 0;
    int end = arr.size() - 1;

    quicksort(arr, st, end);

    for(int val : arr) {
        cout << val << " ";
    }
}
