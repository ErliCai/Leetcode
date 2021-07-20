class ListNode():
    def __init__(self, val = 0, next = None):
        self._val = val
        self._next = next

    def get_val(self):
        return self._val

    def get_next(self):
        return self._next

class MyLinkedList(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self._head = None
        self._len = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self._len:
            return -1

        curr = self._head
        while index > 0:
            curr = curr._next
            index -= 1
        return curr._val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_head = ListNode(val = val, next = self._head)
        self._head = new_head
        self._len += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self._len == 0:
            self.addAtHead(val)
        else:
            curr = self._head
            while curr._next:
                curr = curr._next
            curr._next = ListNode(val=val)
            self._len += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self._len:
            return
        elif index == self._len:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr = self._head
            while index > 1:
                curr = curr._next
                index -= 1
            new_node = ListNode(val)
            curr._next, new_node._next = new_node, curr._next
            self._len += 1
            

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            self._head = self._head._next
            self._len -= 1
        elif index < self._len:
            curr = self._head
            while index > 1:
                curr = curr._next
                index -= 1
            curr._next = curr._next._next
            self._len -= 1
 


L = MyLinkedList()
L.addAtHead(1)
L.addAtTail(3)
L.addAtIndex(1,2)
print(L._head._next._val)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)