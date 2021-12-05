from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print(self.dict)
        if len(self.dict) == self.capacity and key not in self.dict:
            self.dict.popitem(last=False)
        self.dict[key] = value
        self.dict.move_to_end(key)
