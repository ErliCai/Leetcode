# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        duplicate = dict()

        pointer = head
        while pointer:
            if pointer.val not in duplicate:
                duplicate[pointer.val] = False
            else:
                duplicate[pointer.val] = True
            pointer = pointer.next

        dummyNode = ListNode(-101, head)

        curr = dummyNode
        next = curr.next
        while next:
            if duplicate[next.val]:
                curr.next = next.next
                next = next.next
            else:
                curr, next = next, next.next

        curr.next = None
        return dummyNode.next


        