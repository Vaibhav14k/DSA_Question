#include<iostream>
#include<list>
using namespace std;

class Node{
    public:
        int data;
        Node* next;
        Node(int val){
            data = val;
            next =  NULL;
        }
};
class List {
    Node* head;
    Node* tail;
    public : 
    List(){
        head = tail = NULL;
    }
    void push_front(int val){
        Node* newNode = new Node(val);
        if ( head == NULL){
            head = tail = newNode;
            return ;
        }
        else {
            newNode->next = head; //
            head = newNode;
        }
    }

    void insert ( int val , int position){
        if(position<0){
            cout<<"invalid position";
        }else if(position ==0){
            push_front(val);
        }else{
            Node* temp=head;
            for(int i=0;i<position-1;i++){
                temp=temp->next;
            }
            Node* newnode = new Node(val);
            newnode->next=temp->next;
            temp->next = newnode;
        }
    }
    int search(int key){
        Node* temp = head;
        int idx=0;
        while(temp != NULL){
            if (  temp->data == key  ){
                return idx;
            }
            else {
                temp = temp->next;
                idx++;
            }
        }
        return -1;
    }

    void printll(){
        Node* temp = head;
        while (temp != NULL) {
            cout<< temp->data << "->" ;
            temp =temp->next;
        }
        cout << " NULL " << endl;
    }
};

int  main(){
    List ll;
    ll.push_front(30);
    ll.push_front(20);
    ll.push_front(10);
    ll.insert(15,2);
    ll.printll();
    cout<<ll.search(1);

    return 0;
}