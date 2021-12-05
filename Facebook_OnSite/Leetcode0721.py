class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        

        email_name = {}
        name_email = {}

        for a in accounts:
            name = a[0]
            emails = a[1:]

            if name not in name_email:
                name_email[name] = []
            name_email[name].append(set(emails))

        for name in name_email:
            self.find(name_email[name])

        rst = []
        for name in name_email:
            rst += [[name] + sorted(list(i)) for i in name_email[name]]

        #print(rst)

        return rst

    def find(self, emails):
        
        visited_email = set()
        i = 0
        while i < len(emails):
            same_user = []
            next_emails = []
            for k in emails[i]:
                if k not in visited_email:
                    visited_email.add(k)
                    next_emails.append(k)
            while next_emails:
                e = next_emails.pop()
                for j in range(i+1, len(emails)):
                    email = emails[j]
                    if e in email:
                        for e2 in email:
                            if e2 not in visited_email:
                                visited_email.add(e2)
                                next_emails.append(e2)
                        if j not in same_user:
                            same_user.append(j)
            same_user.sort()
            for user in same_user[::-1]:
                email2 = emails.pop(user)
                emails[i] = emails[i].union(email2)

            i += 1

S = Solution()
accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
#accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
S.accountsMerge(accounts)

