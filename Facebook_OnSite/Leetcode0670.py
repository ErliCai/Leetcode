class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num_string = str(num)
        max_id = []
        maximum = -1
        for i in range(len(num_string)):
            if int(num_string[-1-i]) > maximum:
                max_id.append(-1-i)
                maximum = int(num_string[-1-i])
            else:
                max_id.append(max_id[-1])

        max_id = max_id[::-1]
        maximum = toswap = None
        for i in range(len(num_string) - 1):
            if num_string[i] < num_string[max_id[i]] and i != max_id[i]:
                maximum, toswap = len(max_id) + max_id[i], i
                break

        new_num = ""
        for i in range(len(num_string)):
            if i == maximum:
                new_num += num_string[toswap]
            elif i == toswap:
                new_num += num_string[maximum]
            else:
                new_num += num_string[i]

        return int(new_num)


S = Solution()
num = 2736
print(S.maximumSwap(num))

num = 115
print(S.maximumSwap(num))