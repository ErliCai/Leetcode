class Solution(object):    
    def reverseList(self, head):
        if not head:
            return head
        
        prev = None
        curr = head
        next = curr.next

        while next:
            curr.next = prev
            prev, curr, next = curr, next, next.next
            
        curr.next = prev
        
        return curr

    def reverseList(self, head):
        if not head:
            return head

        if not head.next:
            return head
        else:
            h = rl = self.reverseList(head.next)
            while rl.next:
                rl = rl.next

            rl.next = head
            head.next = None
            return h

