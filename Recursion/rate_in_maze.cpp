#include<iostream>
#include<vector>
using namespace std;

void helper(vector<vector<int>> &mat, int r, int c, vector<string> &ans, string path) {
    int n = mat.size();

    // Check bounds and whether the cell is blocked or already visited
    if (r < 0 || c < 0 || r >= n || c >= n || mat[r][c] != 1)
        return;

    // Destination reached
    if (r == n - 1 && c == n - 1) {
        ans.push_back(path);
        return;
    }

    // Mark visited
    mat[r][c] = -1;

    // Explore in all four directions
    helper(mat, r + 1, c, ans, path + "down "); // down
    helper(mat, r - 1, c, ans, path + "UP "); // up
    helper(mat, r, c + 1, ans, path + "right "); // right
    helper(mat, r, c - 1, ans, path + "left "); // left

    // Backtrack
    mat[r][c] = 1;
}

vector<string> findpath(vector<vector<int>> &mat) {
    vector<string> ans;
    string path = "";
    if (mat[0][0] == 1) {
        helper(mat, 0, 0, ans, path);
    }
    return ans;
}

int main() {
    vector<vector<int>> mat =  {{1,0,0,0},
                                {1,1,0,1},
                                {1,1,0,0},
                                {0,1,1,1}};
    
    vector<string> paths = findpath(mat);
    
    for (string p : paths) {
        cout << p << endl;
    }

    return 0;
}
