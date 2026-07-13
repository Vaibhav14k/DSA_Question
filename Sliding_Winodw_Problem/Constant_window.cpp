#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> arr = {2, 5, 1, 8, 2, 9, 1};
    int k = 3;
    int n = arr.size();
    int l = 0;
    int r = k - 1;
    int sum = 0;
    int startidx;
    for (int i = 0; i < k; i++)
    {
        sum += arr[i];
    }
    int maxsum = sum;
    while (r < n - 1)
    {
        r++;
        sum += arr[r];
        sum -= arr[l];
        l++;
        if(sum>maxsum){
            maxsum = sum;
            startidx = l;
        }
    }
    cout << "maxlength of subarray is : " << maxsum<<endl;

    cout<<"subarray ";
    for(int i=startidx;i<startidx+k ;i++){
        cout<<arr[i]<< " ";
    }
    return 0;
}