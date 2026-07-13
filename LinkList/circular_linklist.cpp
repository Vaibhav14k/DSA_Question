#include<iostream>
#include<list>
using namespace std;
class node{
    public : 
    int data ;
    node* next;
    node(int val){
        data = val;
        next = NULL;
    }
};
class circularll{
    node* head;
    node* tail;
    public : 
        circularll(){
            head = tail = NULL;
        }
        void insert_at_head(int val){
            node* newnode = new node(val);
            if ( head == NULL) {
                head = tail = newnode ;
                tail -> next = head ; 
            }
            else {
                newnode ->next = head;
                head = newnode;
                tail -> next = head;
            }
        }
        void insert_at_tail(int val ){
            node* newnode = new node( val ) ; 
            if ( head == NULL ){
                head =  tail = newnode ;
            }
            tail -> next = newnode ;
            tail = newnode;
            newnode ->  next = head ;
        }
        void delete_the_head(){
            if ( head  == NULL  ){
                cout << " ll is not exit  ";
            }
            else if ( head == tail ){
                delete head;
                head = tail = NULL;
            }
            else {
                node* temp = head;
                head = head -> next;
                tail -> next = head ;
                temp->next = NULL ;
                delete temp;
            }
        }
        void delete_the_tail(){
            if ( head == NULL){
                cout << " list is not exist ";
            }
            else if ( head == tail ){
                delete tail;
                head = tail = NULL;
            }
            else {
                node* temp = tail;
                node* prev = head;
                while ( prev->next != tail ){
                    prev = prev->next;
                }
                tail = prev ;
                tail -> next = head;
                temp->next = NULL;
                delete temp;
            }
        }
        void print(){
            if ( head == NULL  ) cout<<"li is not exist";
            cout << head->data<<"->";
            node* temp = head->next;
            while ( temp != head){
                cout << temp->data << " -> ";
                temp= temp->next;
            }
            cout<< head -> data  << endl;
        }
};
int main(){
    circularll cll;
    cll.insert_at_head(3);
    cll.insert_at_head(2);
    cll.insert_at_head(1);
    cll.insert_at_tail(10);
    cll.print();
    // cll.delete_the_head();
    cll.delete_the_tail();
    cll.print();
}