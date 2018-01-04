'''
Input: k = 3, n =  4
list1 = 1->3->5->7->NULL
list2 = 2->4->6->8->NULL
list3 = 0->9->10->11

Output:
0->1->2->3->4->5->6->7->8->9->10->11
'''

from Queue import PriorityQueue

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class llist:
    def mergekLists_PriorityQueue(self,lists):
        head = point = Node(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val,l))
        while not q.empty():
            val,node = q.get()
            point.next = Node(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,node))
        return head.next
    def mergekLists(self,rootLists):
        root = []
        for i in rootLists:
            root = self.mergeTwoLists(root,i)
        return root

    def printList(self,root):
        while root.next is not None:
            print root.val,' -> ',
            root = root.next
        print root.val
    def mergeTwoLists(self, root1, root2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = Node(0)
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in xrange(len(lists)):
            l = lists[i]
            while l != None:
                res.append(l)
                l = l.next
        res = sorted(res, key = lambda x : x.val)
        for i in xrange(len(res) -1):
            res[i].next = res[i + 1]
        if len(res) > 0:
            res[-1].next = None
            return res[0]
        return None
def main():
    root1 = Node(0)
    root1.next = Node(9)
    root1.next.next = Node(10)
    root1.next.next.next = Node(11)
    root2 = Node(1)
    root2.next = Node(3)
    root2.next.next = Node(5)
    root2.next.next.next = Node(7)
    root3 = Node(2)
    root3.next = Node(4)
    root3.next.next = Node(6)
    root3.next.next.next = Node(8)
    root = llist().mergekLists_PriorityQueue([root1,root2,root3])
    return root
if __name__ == '__main__':
    llist().printList(main())
