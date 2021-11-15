
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        original = []
        new = []
        
        h = head
        dummyHead = Node(0)
        curr = dummyHead

        while h:
            curr.next = (Node(h.val))
            curr = curr.next
            original.append(h)
            new.append(curr)
            h = h.next

        h = head
        curr = dummyHead.next
        while h:
            r = h.random
            if r is not None:
                i = original.index(r)
                curr.random = new[i]

            h, curr = h.next, curr.next

        return dummyHead.next

        

class Solution2(object):
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        if head not in self.map:
            new_node = Node(head.val)
        else:
            new_node = self.map[head]

        self.map[head] = new_node 

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node
