#include<iostream>
#include<vector>
using namespace std;
class node{
    public:
    int data;
    node* left;
    node* right;
    node(int val){
        data= val;
        left = right= NULL;
    }
};
static int idx=-1;
node* binarytree(vector<int> preorder){
    idx++;
    if(preorder[idx]==-1){
        return NULL;
    }
    node* root = new node(preorder[idx]);
    root->left = binarytree(preorder);
    root->right = binarytree(preorder);
    return root;
}
void postorder(node* root){
    if(root==NULL){
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout<<root->data<<" ";
}
int main(){
    vector<int>preoder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = binarytree(preoder);
    // cout<<root->data<<" ";
    cout<<endl;
    postorder(root);
    return 0;
}