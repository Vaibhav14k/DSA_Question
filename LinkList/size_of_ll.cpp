#include<iostream>
#include<list>
using namespace std; 

class node{
    public : 
        int val;
        node* next;
        node(int data){
            val = data;
            next = NULL;
        }
};
class List {
        node* head;
        node* tail;
        public : 
            List(){
                head = tail = NULL;
            }
            void push_front(int data){
                node* newNode = new node(data);
                if ( head == NULL){
                    head = tail = newNode;
                    return ;
                }
                else {
                    newNode->next = head;
                    head = newNode;
                }
            }
            void push_back(int   data ){
                node* newNode = new node(data);
                if ( head == NULL){
                    head = tail = newNode;
                }
                else {
                    tail ->next = newNode;
                    tail = newNode;
                }
            }
            void pop_back(){
                
            }

            void printll(){
                node* temp = head;
                int idx=0;
                while ( temp != NULL){
                    cout<< temp->val << "-> ";
                    temp = temp->next;
                    idx++;

                }
                cout<<"NULL" << endl;
                cout<<"number of nodes  in linklist" << idx ;
            }
    };
int main(){
    List ll;
    ll.push_front(3);
    ll.push_front(2);
    ll.push_front(1);
    ll.printll();
}