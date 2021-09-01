# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        l = 1
        h = head
        while h.next:
            l += 1
            h = h.next

        dummy_head = ListNode(-float("inf"), head)
        for i in range(l):
            h = dummy_head
            for j in range(i):
                h = h.next
            node = h.next
            h.next = node.next

            h = dummy_head
            j = 0
            while j < i:
                if h.next.val > node.val:
                    h.next, node.next = node, h.next
                else:
                    h = h.next

        return dummy_head.next

        