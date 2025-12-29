#include <iostream>
#include <queue>
using namespace std;

class MyStack {
    queue<int> q1;
    queue<int> q2;

public:
    MyStack() {
        // Constructor
    }

    void push(int x) {
        // Move all elements from q1 to q2
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        // Push new element to q1
        q1.push(x);
        // Move everything back to q1
        while (!q2.empty()) {
            q1.push(q2.front());
            q2.pop();
        }
    }

    int pop() {
        if (!q1.empty()) {
            int val = q1.front();
            q1.pop();
            return val;
        }
        return -1; // Error condition
    }

    int top() {
        if (!q1.empty()) {
            return q1.front();
        }
        return -1; // Error condition
    }

    bool empty() {
        return q1.empty();
    }
};

// Test the MyStack class
int main() {
    MyStack* obj = new MyStack();

    obj->push(10);
    obj->push(20);
    obj->push(30);

    cout << "Top element: " << obj->top() << endl;   // 30
    cout << "Popped: " << obj->pop() << endl;        // 30
    cout << "Top element now: " << obj->top() << endl; // 20
    cout << "Is empty? " << (obj->empty() ? "Yes" : "No") << endl; // No

    delete obj;
    return 0;
}
