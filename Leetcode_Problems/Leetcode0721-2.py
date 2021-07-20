from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        graph = defaultdict(set)
        email_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_name[email] = name

        answer = []
        visited = set()
        for email in graph:
            if email not in visited:
                s = {email}
                visited.add(email)
                name = email_name[email]
                emails = [email]
                while s:
                    e = s.pop()
                    for next_e in graph[e]:
                        if next_e not in visited:
                            visited.add(next_e)
                            s.add(next_e)
                            emails.append(next_e)

                answer.append([name] + sorted(emails))

        return answer

    
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
S = Solution()
#S.accountsMerge(accounts)
print(S.accountsMerge(accounts))


