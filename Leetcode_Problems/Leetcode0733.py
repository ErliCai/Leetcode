class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        q = [(sr, sc)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.pop()
            image[x][y] = newColor
            for dx, dy in directions:
                newx, newy = x+dx, y+dy
                if 0 <= newx < m and 0 <= newy < n and image[newx][newy] == color:
                    q.append((newx, newy))

        return image