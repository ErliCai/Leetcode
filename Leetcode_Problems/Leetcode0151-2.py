class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.split()
        return " ".join(s[::-1])


class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        rst = ""

        buffer = ""
        for c in s:
            if c == " " and buffer != "":
                rst = buffer + " " + rst
                buffer = ""
            elif c != " ":
                buffer += c

        if buffer != " ":
            rst += buffer

        return rst