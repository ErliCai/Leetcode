class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        
        a,b = "a","b"
        if a < b:
            a,b = b,a
            a,b = "b","a"

        duplicated = a - b
        
        s = ""
        for i in range(b):
            if i < duplicated:
                s += 2 * a
                s += b
            else:
                s += a
                s += b

        return s