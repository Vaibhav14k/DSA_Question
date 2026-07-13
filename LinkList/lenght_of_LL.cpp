#include<iostream>
using namespace std;
class node{
    public :
    int data;
    node* next;
    node(int val){
        data=val;
        next=NULL;
    }
};
class list{
    private :
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
        }else{
            tail->next = newnode;
            tail = newnode;
        }
    }
    void print(){
        node* temp = head;
        int count=0;
        while(temp != NULL){
            cout<<temp->data<<"->";
            temp = temp->next;
            count++;
        }
        cout<<"NULL\n";
            cout<< "lenght of link list : "<< count;
    }
};
int main(){
    list ll;
    ll.push_back(40);
    ll.push_back(30);
    ll.push_back(20);
    ll.push_back(10);
    ll.print();
}