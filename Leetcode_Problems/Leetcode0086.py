# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dividor = ListNode(0,head)
        dummyHead = ListNode(0, dividor)

        less, curr = dummyHead, dividor
        next = curr.next

        while next:
            if next.val < x:
                curr.next = next.next
                less.next, next.next = next, dividor
                less, next = next, curr.next
            else:
                curr, next = next, curr.next

        less.next = dividor.next

        return dummyHead.next