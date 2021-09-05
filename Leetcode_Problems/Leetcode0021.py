# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummyHead = ListNode()
        cur = dummyHead
        while l1 and l2:
            #print(dummyHead)
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
            cur.next = None
                
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        return dummyHead.next