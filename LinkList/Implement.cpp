#include <iostream>
#include <vector>
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
class list
{
    Node *head;
    Node *tail;

public:
    list()
    {
        head = tail = NULL;
    }
    void push_front(int val)
    {
        Node *newnode = new Node(val);
        if (head == NULL)
        {
            head = tail = newnode;
        }
        else
        {
            newnode->next = head;
            head=newnode;
        }
    }
    void push_back(int val)
    {
        Node* newnode = new Node(val);
        if(head==NULL){
            head=tail=newnode;
        }else{
            tail->next = newnode;
            tail = newnode;
        }
    }
    void pop_front(){
        Node* temp=head;
        if(head==NULL){
            return ;
        }else{
            head = head->next;
            temp->next = NULL;
        }
    }
    void pop_back(){
        Node* temp=head;
        if(tail==NULL){
            return;
        }
        while(temp->next != tail){
            temp = temp->next;
        }
        temp->next = NULL;
    }
    void print()    
    {
        Node *temp = head;
        while (temp != NULL)
        {
            cout << temp->data << "-> ";
            temp = temp->next;
        }
        cout << "NULL\n";
    }
};
int main()
{
    list ll;
    // ll.push_front(10);
    // ll.push_front(20);
    // ll.push_front(30);
    ll.push_back(10);
    ll.push_back(20);
    ll.push_back(30);
    // ll.pop_front();
    ll.pop_back();
    ll.print();
}