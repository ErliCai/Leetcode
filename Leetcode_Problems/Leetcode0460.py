from collections import deque
from collections import OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain_capacity = capacity
        self.key_to_freq = {}
        self.freq_to_key = {0:OrderedDict()}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.freq:
            return -1
        
        f = self.key_to_freq[key]
        val = self.freq_to_key[f][key]
        del self.freq_to_key[f][key]
        if f + 1 not in self.freq_to_key:
            self.freq_to_key[f+1] = OrderedDict()
        self.freq_to_key[f+1][key] = val
        self.freq_to_key[f+1].move_to_end(key, last = False)

        return val

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.remain_capacity > 0:
            if key not in self.key_to_freq:
                self.freq_to_key[0][key] = value
                self.remain_capacity -= 1
            self.get(key)
        else:
            if key in self.key_to_freq:
                self.get(key)
            else:
                for f in self.freq_to_key:
                    return
            
        

d = OrderedDict()
d[0] = 0
d[1] = 1
del d[1]
print(d)

if d:
    print(1)
del d[0]
if d:
    print(0)