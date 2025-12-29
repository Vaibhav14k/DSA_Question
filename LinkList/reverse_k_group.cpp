#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head ;
        int cnt=0;
        while (cnt< k){
            if ( temp== NULL){
                return head;
            }
            temp= temp->next;
            cnt++;
        }
        ListNode* prevnode = reverseKGroup(temp,k);
        temp= head;
        cnt =0;
        while ( cnt <k ){
            ListNode* nextnode = temp -> next;
            temp->next = prevnode ;
            prevnode = temp;
            temp = nextnode;
            cnt++;
        }
        return prevnode;
    }
};

// Helper function to print the list
void printList(ListNode* head) {
    while (head) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "NULL\n";
}

// Helper function to create a linked list from array
ListNode* createList(int arr[], int size) {
    if (size == 0) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* current = head;
    for (int i = 1; i < size; i++) {
        current->next = new ListNode(arr[i]);
        current = current->next;    
    }
    return head;
}

int main() {
    Solution sol;
    int arr[] = {1, 2, 3, 4, 5};
    int k = 2;
    ListNode* head = createList(arr, sizeof(arr)/sizeof(arr[0]));

    cout << "Original list:\n";
    printList(head);

    ListNode* result = sol.reverseKGroup(head, k);

    cout << "List after reversing in groups of " << k << ":\n";
    printList(result);

    return 0;
}
