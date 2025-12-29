#include<iostream>
#include<list>
using namespace std ;
class node {
    public: 
        int data;
        node* next;
        node* prev;
        node(int val){
            data= val;
            next=prev=NULL;
        }
};
class doubleyLL{
    node* head;
    node* tail;
    public: 
    doubleyLL(){
        head = tail = NULL;
    }
    void push_front(int val){
        node* newnode = new node(val);
        if(head==NULL){
            head=tail=newnode;
        }else{
            newnode->next = head;
            head->prev = newnode ;
            head = newnode ;
        }
    }
    void push_back(int val){
        node* newnode  = new node(val);
        if(head==NULL){
            head=tail=newnode;
        }else{
            tail->next = newnode ;
            newnode->prev = tail;
            tail = newnode;
        }
    }
    void pop_fornt(){
        node* temp = head;
        if(head==NULL){
            cout<<"link list is empty ";
        }else{
            head = head->next;
            temp->next = NULL;
            head->prev = NULL;
        }
    }
     void pop_back() {
        if (tail == NULL) {
            cout << "List is empty\n";
            return;
        }
        node* temp = tail;
        if (head == tail) { // only one node
            head = tail = NULL;
        } else {
            tail = tail->prev;
            tail->next = NULL;
        }
        delete temp;
    }
    void print(){ 
        node* temp = head;
        while (temp != NULL) {
            cout << temp -> data << " < = >  ";
            temp = temp ->next;
        }
        cout<<"NULL"<< endl;
    }
};
int main(){
    doubleyLL dll;
    // dll.push_front(3);
    // dll.push_front(2);
    // dll.push_front(1);
    dll.push_back(30);
    dll.push_back(20);
    dll.push_back(10);
    dll.print();
    // dll.pop_fornt();
    dll.pop_back();
    dll.print();

}