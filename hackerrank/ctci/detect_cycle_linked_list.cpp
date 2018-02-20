/*
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named that points to the head of a linked list.
Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.

Note: If the list is empty, head will be null.
*/

// --------------Do this some other day-----------------------
// #include<string>
// #include<iostream>
// using namespace std;
// struct Node{
//   int data;
//   struct Node* next;
// };
//
//
// int main(){
//   string numList;
//   getline(cin,numList);
//   num
//   cout<<numList;
// }


/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as:
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    if(head==NULL || head->next == NULL) return false;
    Node* fast,*slow;
    fast = head;
    slow = head;
    fast = fast->next->next;
    while(fast->next->next!=NULL and fast!=slow)
    {
      fast = fast->next->next;
      slow = slow->next;
    }
    if(fast == slow)
    {
      return true;
    }
    else return false;
}
