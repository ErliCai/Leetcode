# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def reverList(l):
            curr, prev = l, None
            if l.next:
                nex = l.next
                curr.next = prev
                curr, prev = nex, curr

            curr.next = prev
            return curr

        l1 = reverList(l1)
        l2 = reverList(l2)

        dummyHead = ListNode()
        curr = dummyHead
        carry = False
        while l1 or l2:
            s = 0
            if carry:
                s += 1
                carry = False
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s >= 10:
                carry = True
            curr.next = ListNode(s % 10)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        
        return reverList(dummyHead.next)
