#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> arr = {2, 5, 1, 8, 2, 9, 1};
    int k = 14;
    int n = arr.size();
    int left = 0;
    int sum = 0;
    int maxlen= 0 ;
    int startidx = 0;
    int endidx = 0;
    for(int right = 0; right<n ;right++){
        sum += arr[right];
        if(sum>k){
            sum -= arr[left];
            left++;
        }
        if( right - left + 1 > maxlen ){
            maxlen = right - left + 1;
            startidx = left;
            endidx = right;
        }
    }
      cout << "Maximum Length = " << maxlen << endl;

    cout << "Longest Subarray: ";

    for (int i = startidx; i <= endidx; i++)
    {
        cout << arr[i] << " ";
    }
}
