#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n=heights.size();
        cout<<"length"<<n<<endl;
        vector<int>right(n,n);
        vector<int>left(n,0);
        stack<int>s;
        //right : 
        for(int i=n-1;i>=0;i--){
            while(s.size()>0 && heights[s.top()] >= heights[i] ){
                s.pop();
            }
            if(s.size()==0){
                right[i] = n;
            }
            else{
                right[i]=s.top();
            }
            s.push(i);
        }
        //for left : 
        for(int i=0;i<n;i++){
            while(s.size()>0 && heights[s.top()] >= heights[i] ){
                s.pop();
            }
            if(s.size()==0){
                left[i] = -1;
            }
            else{
                left[i]=s.top();
            }
            s.push(i);
        }
        // 
        for(int i=0;i<n;i++){
            int width = right[i] - left[i] -1;
            int rect = heights[i] * width;
            cout<< rect << endl;
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
