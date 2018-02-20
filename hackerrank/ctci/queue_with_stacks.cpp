/*
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

    Enqueue: add a new element to the end of the queue.
    Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process queries, where each query is one of the following types:

    1 x: Enqueue element x into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.

    Sample Input
    10
    1 42
    2
    1 14
    3
    1 28
    3
    1 60
    1 78
    2
    2
    Sample Output
    14
    14

*/

#include<stack>
#include<iostream>
using namespace std;
class MyQueue {

    public:
        stack<int> stack_newest_on_top, stack_oldest_on_top;
        void push(int x) {
          if(stack_newest_on_top.size()==0) stack_newest_on_top.push(x);
          else stack_oldest_on_top.push(x);
        }
        void pop() {
          stack_newest_on_top.pop();
          if(stack_newest_on_top.size() == 0)
          while(stack_oldest_on_top.size()!=0)
          {
            stack_newest_on_top.push(stack_oldest_on_top.top());
            stack_oldest_on_top.pop();
          }
        }

        int front() {
          return stack_newest_on_top.top();
        }
};

int main() {
    MyQueue q1;
    int q, type, x;
    cin >> q;

    for(int i = 0; i < q; i++) {
        cin >> type;
        if(type == 1) {
            cin >> x;
            q1.push(x);
        }
        else if(type == 2) {
            q1.pop();
        }
        else cout << q1.front() << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
