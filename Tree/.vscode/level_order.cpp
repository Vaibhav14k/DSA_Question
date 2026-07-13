#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class node{
    public :
    int data;
    node* left;
    node* right;
    node(int val){
        data=val;
        left=right=NULL;
    }
};
int idx=-1;
node* buildtree(vector<int>preorder){
    idx++;
    if(preorder[idx] == -1){
        return NULL;
    }
        node* root = new node(preorder[idx]);
        root->left = buildtree(preorder);
        root->right = buildtree(preorder);
    return root;
};
void level(node* root){
    queue<node*>q;
    q.push(root);
    q.push(NULL);
    while(!q.empty()){
        node* curr= q.front();
        q.pop();
        if(curr == NULL){
            if(!q.empty()){
                cout<<endl;
                q.push(NULL);
                continue;;
            }else{
                break;
            }
        }
        cout<<curr->data<<" ";
        if(curr->left != NULL){
            q.push(curr->left);
        }
        if(curr->right != NULL){
            q.push(curr->right);
        }
    }   
}
// output : 
// 1
// 2 3
// 4 5 
int main(){
    vector<int>preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = buildtree(preorder);
    level(root);
}