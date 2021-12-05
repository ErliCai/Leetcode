
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        h = head
        d = {}
        dummyHead = Node(0)
        new_h = dummyHead
        while h:
            new_h.next = Node(h.val, h.next)
            new_h = new_h.next
            d[h] = new_h
            h = h.next

        h = head
        new_h = dummyHead.next
        while h:
            if h.random is None:
                new_h.random = None
            else:
                new_h.random = d[h.random]

            h = h.next
            new_h = new_h.next

        return dummyHead.nextn