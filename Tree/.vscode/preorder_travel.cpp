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
static int idx=-1;
node* binarytree(vector<int> preorder){
    idx++;
    if(preorder[idx]==-1) return NULL;
    node* root = new node(preorder[idx]);
    root->left = binarytree(preorder);// left : 
    root->right = binarytree(preorder); // right : 
    return root;
};
// preorder travels : 
void  preOrder(node* root){
    if(root == NULL) {
        return;
    }
    cout<<root->data<<" ";
    preOrder(root->left);
    preOrder(root->right);
}

int main(){
    vector<int>preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    
    node* root = binarytree(preorder);
    preOrder(root);

    
}