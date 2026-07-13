#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

int main() {
    Node* node1 = new Node(10);
    Node* node2 = new Node(20);
    node1->next = node2;

    cout << "node1 data: " << node1->data << endl;
    cout << "node1 address: " << node1 << endl;
    cout << "node1->next (points to node2): " << node1->next << endl;
    cout << "node2 data: " << node2->data << endl;
    cout << "node2 address: " << node2 << endl;
    cout << "node2->next: " << node2->next << endl;  // Should be NULL

    return 0;
}
