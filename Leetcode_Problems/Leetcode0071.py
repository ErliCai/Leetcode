class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        

        drirectory = path.split("/")

        path = [""]
        for d in drirectory:
            if d == "":
                pass
            elif d == ".":
                pass
            elif d == "..":
                n = len(path)
                if n > 1:
                    path = path[:n-1]
            else:
                path.append(d)

        if len(path) == 1:
            path = [""] + path

        return "/".join(path)