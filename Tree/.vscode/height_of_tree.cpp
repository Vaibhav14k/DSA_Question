#include<iostream>
#include<vector>
using namespace std;
class node{
    public :
    int data;
    node* right;
    node* left;
    node(int val){
        data = val;
        left = right = NULL;
    }
};
int idx=-1;
node* buildtree(vector<int>preorder){
    idx++;
    if(preorder[idx]== -1 ){
        return NULL;
    }
    node* root = new node(preorder[idx]);
    root->left = buildtree(preorder);
    root ->right = buildtree(preorder);
    return root;
    
}
void preoder(node* root){
    if(root==NULL){
        return;
    }
        cout<<root->data<<" ";
        preoder(root->left);
        preoder(root->right);
    
}
// height of treee : 
int height(node* root){
    if(root == NULL) return 0;
    int lefth = height(root->left);
    int righth = height(root->right);
    return max(lefth,righth)+1;
}
// sum of tree : 
int sum(node* root){
    if(root==NULL){
        return 0;
    }
    int lefts = sum(root->left);
    int rights= sum(root->right);
    return lefts + rights + root->data ;
}
int main(){
    vector<int> preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = buildtree(preorder);
    preoder(root);
    cout<<endl;
    cout<<"height = "<<height(root);
    cout<<endl;
    cout<<"sum="<<sum(root);
}