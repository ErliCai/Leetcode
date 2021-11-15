class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        ans = []
        for s in strings:
            if ans == []:
                ans.append([s])
            else:
                appended = False
                for l in ans:
                    if self.compare(l[0], s):
                        l.append(s)
                        appended = True
                if not appended:
                    ans.append([s])
            
        return ans 
        
    def compare(self, s1, s2):
        if len(s1) != len(s2):
            return False

        n = (ord(s1[0]) - ord(s2[0])) % 26
        for i in range(len(s1)):
            if (ord(s1[i]) - ord(s2[i])) % 26 != n:
                return False

        return True
