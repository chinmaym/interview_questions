'''
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def mergeTwoLists(self, root1, root2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if root1 is None and root2 is None:
#             return []
#         if root1 is None:
#             return root2
#         if root2 is None:
#             return root1
#         temp1 = temp2 = None
#         temp1 = temp2 = None
#         if root1.val > root2.val:
#         	temp1 = root2
#         	root2 = root1
#         	root1 = temp1
#         start = root1
#         while root1.next is not None and root2 is not None:
#         	if root1.val <= root2.val and root1.next.val > root2.val:
#         		temp1 = root1.next
#         		temp2 = root2.next
#         		root1.next = root2
#         		root2.next = temp1
#         		root1 = root2
#         		root2 = temp2
#         	else:
#         		root1 = root1.next

#         if root1.next is None:
#         	root1.next = root2
#         return start

class Solution(object):
    def mergeTwoLists(self, root1, root2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        cur = start
        while root1 or root2:
        	if root1 and root2:
        		if root1.val < root2.val:
        			cur.next = root1
        			root1 = root1.next
        		else:
        			cur.next = root2
        			root2 = root2.next
        	elif root1:
        		cur.next = root1
        		root1 = root1.next
        	elif root2:
        		cur.next = root2
        		root2 = root2.next
        	cur = cur.next
        return start.next

def printList(root):
	while root is not None:
		print root.val," "
		root = root.next

if __name__=="__main__":
	root1 = ListNode(2)
	root2 = ListNode(1)
	printList(Solution().mergeTwoLists(root1,root2))