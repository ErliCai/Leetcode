class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        invalid_left = invalid_right = 0

        p_count = 0
        for i in s:
            if i == "(":
                p_count += 1
            else:
                p_count -= 1
                invalid_right = min(invalid_right, p_count)

        if p_count > 0:
            invalid_left = p_count
        return invalid_left - invalid_right