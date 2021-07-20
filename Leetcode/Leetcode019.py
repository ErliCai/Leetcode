# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0,head)

        nprev = curr = dummyHead
        for i in range(n+1):
            curr = curr.next

        while curr:
            curr = curr.next
            nprev = nprev.next

        nprev.next = nprev.next.next

        return dummyHead.next


a = {1,2,3}
print(1 in a)