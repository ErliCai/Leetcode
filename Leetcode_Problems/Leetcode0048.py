class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        center = (len(matrix) - 1) / 2.0

        for i in range(int(center) + 1):
            for j in range(i, int(center) + 1):

                diff_x, diff_y = center - i, center - j
                pos1 = (i, j)
                pos2 = (int(center - diff_y), int(center + diff_x))
                pos3 = (int(center + diff_x), int(center + diff_y))
                pos4 = (int(center + diff_y), int(center - diff_x))
                
                print(pos1,pos2,pos3,pos4)

                temp = matrix[pos1[0]][pos1[1]]
                matrix[pos1[0]][pos1[1]] = matrix[pos4[0]][pos4[1]]
                matrix[pos4[0]][pos4[1]] = matrix[pos3[0]][pos3[1]]
                matrix[pos3[0]][pos3[1]] = matrix[pos2[0]][pos2[1]]
                matrix[pos2[0]][pos2[1]] = temp


        