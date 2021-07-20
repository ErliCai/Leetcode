# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        nodes = []
        curr = head
        while curr.next:
            nodes.append(curr)
            curr = curr.next

        i, j= 0, len(nodes) - 1
        while i < j:
            curr, next, ins = nodes[i], nodes[i].next, nodes[-1]
            curr.next, ins.next = ins, next