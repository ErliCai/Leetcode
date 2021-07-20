# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        gurad = ListNode(0, head)

        pos = 1
        curr = gurad
        
        while pos  < left:
            curr = curr.next
            pos += 1

        node_before_reverse = curr
        tail = curr.next
        
        prev, curr, next = curr, curr.next, curr.next.next
        while pos < right:
            print(prev.val, curr.val, next.val)
            curr.next = prev
            prev, curr, next = curr, next, next.next
            pos += 1
            
        curr.next = prev
        node_before_reverse.next = curr
        tail.next = next
        
        return gurad.next

