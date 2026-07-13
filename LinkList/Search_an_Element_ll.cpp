#include<iostream>
using namespace std;
class node{
    public:
    int data;
    node* next;
    node(int val){
        data=val;
        next=NULL;
    }
};
class list{
    node* head;
    node* tail;
    public:
    list(){
        head=tail=NULL;
    }
    void push_back(int val){
        node* newnode = new node(val);
        if(head==NULL){
            head=tail=newnode;
        }
        tail->next = newnode;
        tail=newnode;
    };
    void print(){
        node* temp= head;
        while(temp != NULL){
            cout<<temp->data<<"->";
            temp = temp->next;
        }
        cout<<"NULL\n";
    }
    bool  search(int key){
        node* temp=head;
        int idx=0;
        while(temp->next != NULL ){
            if(temp->data == key){
                return true;
            }else{
                idx++;
            temp=temp->next;
            }
        }
        return false;
    }
};
int main(){
    list ll;
    ll.push_back(30);
    ll.push_back(20);
    ll.push_back(10);
    ll.print();
    cout<<ll.search(2);
}