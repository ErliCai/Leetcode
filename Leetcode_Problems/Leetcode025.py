class Solution(object):
    def reverse(self, head):
        prev = head
        curr = head.next
        prev.next = None

        while curr:
            next = curr.next
            curr.next = prev
            curr, prev = next, curr

        return prev, head


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        prev = curr = head
        count = 0
        beginning = True
        newhead = None
        newtail = None
        while curr:
            count += 1

            if count == k:
                next = curr.next
                curr.next = None
                h, t = self.reverse(prev)
                if beginning:
                    newhead = h
                    beginning  = False
                else:
                    newtail.next = h
                newtail = t
                prev = curr = next
                count = 0
            else:
                curr = curr.next
                
        newtail.next = prev
        return newhead
    
    