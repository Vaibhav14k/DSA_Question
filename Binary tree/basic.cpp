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
        data= val;
        left = NULL;
        right = NULL;
    }
};

static int idx = -1;
node* buildtree(vector<int> preorder){
    idx++;
    if(preorder[idx]==-1){
        return NULL;
    }
    node* root = new node(preorder[idx]);
    root->left = buildtree(preorder);
    root->right= buildtree(preorder);
    return root;
};

void preorderprint(node* root){
    if(root ==  NULL) return ;
    cout<<root->data<<" ";
    preorderprint(root->left);
    preorderprint(root->right);
    
}

void inorderprint(node* root){
    if(root == NULL) return ;
    inorderprint(root->left);
    cout<<root->data<<" ";
    inorderprint(root->right);
}
void postorderprint(node* root){
    if(root ==NULL) return ;
    postorderprint(root->left);
    postorderprint(root->right);
    cout<<root->data<<" ";
}

void levelprint(node* root){
    queue<node*> q;
    q.push(root);
    while(q.size()>0){     
            node* curr = q.front();
            q.pop();
            cout<<curr->data<<" "; 
            if(curr->left !=NULL){
                q.push(curr->left);
            }
            if(curr->right != NULL){
                q.push(curr->right);
            }
    }
}

int main(){
    vector<int> preorder = {1,2,-1,-1,3,4,-1,-1,5,-1,-1};
    node* root = buildtree(preorder);
    cout << "Preorder traversal of built tree: " ; 
    preorderprint(root);
    cout<<endl;
    cout << "inorder traversal of built tree: " ; 
    inorderprint(root);
    cout<<endl;
    cout << "postorder traversal of built tree: " ; 
    postorderprint(root);
    cout<<endl;
    cout<<"level order travels " ;
    levelprint(root);
    cout<<endl;
}