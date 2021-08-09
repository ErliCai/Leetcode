class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        new_s = ["Dummy", "Dummy"]
        for i in s:
            if i == new_s[-1] and i == new_s[-2]:
                pass
            else:
                new_s.append(i)
        new_s.pop(0)
        new_s.pop(0)
        return "".join(new_s)
