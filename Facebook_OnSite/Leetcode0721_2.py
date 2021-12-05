class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        name_emails = {}
        email_pos = {}
        rst = []

        for account in accounts:
            name = account[0]
            emails = account[1:]
            if name not in name_emails:
                name_emails[name] = []
            name_emails[name].append(emails)
            for e in emails:
                if e not in email_pos:
                    email_pos[e] = len(name_emails[name]) - 1

        for name in name_emails:
            accs = name_emails[name]
            parents = [i for i in range(len(accs))]
            for i in range(len(accs)):
                a = accs[i]
                for email in a:
                    if email_pos[email] < parents[i]:
                        parents[i] = parents[email_pos[email]]

            nums = set(parents)
            for p in nums:
                r = set()
                for i in range(len(parents)):
                    if parents[i] == p:
                        for e in name_emails[name][i]:
                            r.add(e)

                rst.append([name]+sorted(list(r)))
                
                
        return rst

S = Solution()
accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
#accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(S.accountsMerge(accounts))
