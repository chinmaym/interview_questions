'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode():
    def __init__(self,val):
        self.value = val
        self.next = None

class Llist():
    def add(self,node1,node2,carry = 0):
        if not node1 and not node2:
            if carry > 0:
                return ListNode(carry)
            else:
                return None
        elif not node1:
            value = node2.value + carry
            carry = value/10
            value = value%10
            tempNode = ListNode(value)
            tempNode.next = self.add(None,node2.next,carry)
        elif not node2:
            value = node1.value + carry
            carry = value/10
            value = value%10
            tempNode = ListNode(value)
            tempNode.next = self.add(node1.next,None,carry)
        else:
            value = node1.value+node2.value + carry
            carry = value/10
            value = value%10
            tempNode = ListNode(value)
            tempNode.next = self.add(node1.next,node2.next,carry)
        return tempNode
        
    def reprList(self,root):
        valueList = []
        while root is not None:
            valueList.append(root.value)
            root = root.next
        return valueList

def main():
    root1 = ListNode(2)
    root1.next = ListNode(4)
    root1.next.next = ListNode(3)
    root4 = ListNode(0)
    root2 = ListNode(5)
    root2.next = ListNode(6)
    root2.next.next = ListNode(4)
    root3 = Llist().add(root1,root4)
    return Llist().reprList(root3)

if __name__=="__main__":
    print main()
