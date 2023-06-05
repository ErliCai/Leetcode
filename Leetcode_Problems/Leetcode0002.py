# Definition for singly-linked list.
from typing import List


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
        
        carryOn = False
        dummyHead = ListNode()
        curr = dummyHead

        while l1 or l2:
            s = 0
            if carryOn:
                s += 1
            carryOn = False
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s > 10:
                carryOn = True
            curr.next = ListNode(s % 10)
            curr = curr.next

        if carryOn:
            curr.next = ListNode(1)

        return dummyHead.next

            