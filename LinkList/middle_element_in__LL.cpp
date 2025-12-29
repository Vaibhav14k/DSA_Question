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
    void push_front(int val){
        node* newnode = new node(val);
        if(head==NULL){
            head=tail=newnode;
        }else{
            newnode->next = head;
            head= newnode;
        }
        
    }
    void print(){
        node* temp=head;
        while(temp != NULL){
            cout<<temp->data<<"->";
            temp=temp->next;
        }
        cout<<"NULL\n";
    }
    void middle(){
        node* slow=head;
        node* fast=head;
        while(fast != NULL && fast->next != NULL  ){
            slow= slow->next;
            fast= fast->next->next;
        }
        cout<<"middle element : "<< slow->data;
    }
};
int main(){
    list ll;
    ll.push_front(10);
    ll.push_front(20);
    ll.push_front(30);
    ll.push_front(40);
    ll.push_front(50);

    ll.print();
    ll.middle();

}   