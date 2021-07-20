class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        
        boxes = [int(i) for i in boxes]

        r_0 = 0
        for i in range(boxes):
            r_0 += i * boxes[i]

        answer = [r_0]
        for i in range(1, len(boxes)):
            last = answer[-1]
            now = last + sum(boxes[:i]) - sum(boxes[1:])
            answer.append(now)

        return answer

