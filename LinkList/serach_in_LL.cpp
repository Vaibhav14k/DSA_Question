#include<iostream>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
    Node(int val)
    {
        data = val;
        next = NULL;
    }
};
class list{
    Node* head;
    Node* tail;
    public:
    list(){
        head=tail=NULL;
    }
    void push_front(int val){
        Node* newnode = new Node(val);
        if(head==NULL){
            head=tail=newnode;
        }else{
            newnode->next = head;
            head=newnode;
        }
    }
    void insert(int val,int position){
        if(position<0){
            cout<<"invalid ";
        }else if(position == 0){
            push_front(val);
        }else{
            Node* temp = head;
            for(int i=0;i<position-1;i++){
                temp = temp -> next;
            }
            Node* newnode = new Node(val);
            newnode->next = temp->next;
            temp->next = newnode;
        }
    }
    int serach(int key){
        Node* temp = head;
        int idx=0;
        while(temp->next != NULL){
            if(temp->data == key){
                return idx;
            }else{
                temp= temp->next;
                idx++;
            }
        }
        return -1;
    }
    void print(){
        Node* temp=head;
        while(temp != NULL){
            cout<<temp->data<<"-> ";
            temp=temp->next;
        }
        cout << "NULL\n";
    }
};
int main(){
    list ll;
    ll.push_front(10);
    ll.push_front(20);
    ll.push_front(30);
    ll.push_front(40);
    // ll.insert(15,2);
    ll.print();
    cout<<ll.serach(30);
}