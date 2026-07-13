#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int>arr = {1, 2, 1, 1, 1, 3, 2};
    int k = 5;
    int right = 0;
    int left = 0;
    int sum=0;
    int maxleng = 0;
    int n = arr.size();
    while(right<n){
        sum += arr[right];
        if(sum>k){
            sum -= arr[left];
            left ++ ;
        }
        if(sum == k){
            maxleng = max(maxleng,right - left + 1);
        }
        right ++;
    }
    cout<<"maxlegnt is "<<maxleng;
    return 0;
}