#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = NULL;
    }
};

class List {
    Node* head;
    Node* tail;

public:
    List() {
        head = tail = NULL;
    }

    void push_front(int val) {
        Node* newNode = new Node(val);
        if (head == NULL) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head = newNode;
        }
    }

    // Function to print the list
    void print() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }

    // Function to convert linked list into number like 2->4->3 => 342
    int getNumber() {
        Node* temp = head;
        int num = 0;
        int place = 1;
        while (temp != NULL) {
            num += temp->data * place;
            place *= 10;
            temp = temp->next;
        }
        return num;
    }
};

int main() {    
    List l;
    l.push_front(3);
    l.push_front(4);
    l.push_front(2);

    l.print();

    cout << "Number: " << l.getNumber() << endl;

    return 0;
}
