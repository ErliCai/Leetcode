class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        simplified_path = []
        for p in path:
            if p == "":
                pass
            elif p == ".":
                pass
            elif p == "..":
                if len(simplified_path) > 0:
                    simplified_path.pop(-1)
            else:
                simplified_path.append(p)

        return "/" + "/".join(simplified_path)
