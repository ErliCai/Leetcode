class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        self.acum = []
        self.possible_divisions(num, [])
        #print(self.acum)

        signs = ["+", "-", "*", "/"]
        expr = []
        for divisions in self.acum:
            strings = [divisions[0]]
            for i in range(1,len(divisions)):
                new_string = []
                for s in signs[:3]:
                    new_string += [s2 + s + divisions[i] for s2 in strings]
                if divisions[i] != "0":
                    new_string += [s2 + "/" + divisions[i] for s2 in strings]
                strings = new_string
            expr += strings
            #print(divisions, strings)

        ans = []
        for e in expr:
            if eval(e) == target:
                ans.append(e)

        return ans
            
        

    def possible_divisions(self, nums, temp):
        if not nums:
            return

        if nums[0] == "0" and len(nums) != 1:
            self.possible_divisions(nums[1:], temp + [nums[:1]])
        
        if nums[0] != "0" or len(nums) == 1:
            self.acum.append(temp + [nums])
            for i in range(len(nums)):
                self.possible_divisions(nums[i+1:], temp + [nums[:i+1]])

            
S = Solution()
num = "123"
target = 6
print(S.addOperators(num, target))
