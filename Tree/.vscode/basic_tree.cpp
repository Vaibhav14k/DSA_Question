#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class node{
    public:
    int data;
    node* right;
    node* left;
    node(int val){
        data = val;
        right = left = NULL;
    }
};
int idx=-1;
int count=0;
node* buildtree(vector<int>preorder){
    idx++;
    if(preorder[idx]==-1){
        count++;
        return NULL;
    }
    node* root = new node(preorder[idx]);
    root->left = buildtree(preorder);
    root->right = buildtree(preorder);
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
void inorder(node* root){
    if(root==NULL){
        return ;
    }
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
}
int sum=0;
void levelorder(node* root){
    queue<node*>q;
    q.push(root);
    while(q.size()>0){
        node* curr = q.front();
        q.pop();
        cout<<curr->data<<" ";\
        sum += curr->data;
        if(curr->left !=NULL){
            q.push(curr->left);
        }
        if(curr->right != NULL){
            q.push(curr->right);
        }
    }
    cout<<"sum"<<sum;
}
int height(node* root){
    if(root==NULL) return 0;
}
int main(){
    vector<int>preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = buildtree(preorder);
    cout<<"preorder";
    preoder(root);
    cout<<endl;
    cout<<"inorder";
    inorder(root);
    cout<<endl;
    cout<<"levelorde";
    cout<<endl;
    levelorder(root);
    // cout<<root->data<<" "<<endl;
    // cout<<root->left->left->data<<" "<<endl;
    // cout<<root->right->left->data<<" "<<endl;
}