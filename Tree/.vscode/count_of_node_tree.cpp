#include<iostream>
#include<vector>
using namespace std;
class node{
    public: 
    int data;
    node* left;
    node* right;
    node(int val){
        data=val;
        left = right = NULL;
    }
};
int idx=-1;
node* buildtree(vector<int>preorder){
    idx++;
    if(preorder[idx]==-1){
        return NULL;
    }
    node* root = new node(preorder[idx]);
    root->left = buildtree(preorder);
    root->right = buildtree(preorder);
    return root;
}
int count(node* root){
    if(root == NULL) return 0;
    int leftc = count(root->left);
    int rightc = count(root->right);
    return leftc + rightc + 1;
}
int main(){
    vector<int>preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = buildtree(preorder);
    cout<<"count of node = "<<count(root);
}