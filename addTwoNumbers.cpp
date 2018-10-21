#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL) {} 
};

class Solution {
    public:
        ListNode* tail = NULL;
        ListNode* head = NULL;

        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            bool carry = false;
            while(l1 != NULL && l2 != NULL) {
                int val = l1 -> val + l2 -> val;

                if(carry) {
                    val++;
                    carry = false;
                }

                if(val > 9) { //we must subtract and carry
                    val -= 10;
                    carry = true;
                }

                ListNode* temp = new ListNode(val);
                if(head == NULL) {
                    head = tail = temp;
                }
                else {
                    insertAtEnd(temp);
                }

                l1 = l1 -> next;
                l2 = l2 -> next;
            }

            //TODO: functionize this
            while(l1 != NULL) {
                int val = l1 -> val;
                if(carry) {
                    val++;
                    carry = false;
                }

                if(val > 9) { //we must subtract and carry
                    val -= 10;
                    carry = true;
                }
            }

            while(l2 != NULL) {
                int val = l2 -> val;
                if(carry) {
                    val++;
                    carry = false;
                }

                if(val > 9) { //we must subtract and carry
                    val -= 10;
                    carry = true;
                }
            }

            if(carry) { //if we have a carry leftover, then throw it on
                insertAtEnd(new ListNode(1));
            }

            return head;
        }

        void insertAtEnd(ListNode* temp) {
            if(tail == NULL) {
                tail = temp;
            }
            else {
                tail -> next = temp;
                tail = temp;
            }
        }

    void printList() {
        if(head == NULL) {
            cout << "Can't print, no list to print." << endl;
        }
        else {
            ListNode* trav = head -> next;
            cout << head -> val;
            while(trav != NULL) {
                cout << " -> " << trav -> val;
            }
        }
    }

};

int main() {

}