class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if self.isInteger(s) or self.isDecimal(s):
            return True
        if 'e' in s:
            s = s.split('e')
        elif 'E' in s:
            s = s.split('E')
        else:
            return False

        if len(s) != 2:
            return False

        if ((self.isDecimal(s[0]) or self.isInteger(s[0])) and
            self.isInteger(s[1])):
            return True
        return False

    def isInteger(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = str(s)

        if s == "":
            return False
        
        sign = False
        if s[0] == "+" or s[0] == "-":
            sign = True

        starting_pos = 1 if sign else 0

        if len(s) < 1 + starting_pos:
            return False
        else:
            for c in s[starting_pos:]:
                if not (0 <= ord(c) - ord("0") <= 9):
                    return False

        return True

    def isDecimal(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = str(s)

        if s == "":
            return False

        s = s.split(".")
        
        if len(s) != 2:
            return False
        

        if self.isInteger(s[0]) and s[1] == "":
            return True
        elif (self.isInteger(s[0]) 
              and s[1][0] not in ("+", "-") and self.isInteger(s[1])):
            return True
        elif s[0] == "" and len(s[1]) > 0 and s[1][0] not in ("+", "-") and self.isInteger(s[1]):
            return True
        
        
