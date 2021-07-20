class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        name_email = dict()
        answer = []
        for a in accounts:
            if a[0] not in name_email:
                name_email[a[0]] = [sorted(list(set(a[1:])))]

            else:
                name_email[a[0]] += [sorted(list(set(a[1:])))]

        for name in name_email:
            emails = name_email[name]
            length = len(emails)
            email_account = dict()
            for i in range(len(emails)):
                for e in emails[i]:
                    if e in email_account:
                        email_account[e] += [i]
                    else:
                        email_account[e] = [i]
            
            l = [set(i) for i in email_account.values()]

            i = 0
            while i < len(l):
                j = i + 1
                while j < len(l):
                    print(i,j)
                    if l[i].intersection(l[j]):
                        l[i] = l[i].union(l.pop(j))
                        j = i+1
                    else:
                        j += 1
                i += 1

            for s in l:
                e = []
                for i in s:
                    e += emails[i]
                answer.append([name] + sorted(list(set(e))))


        return answer


accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
S = Solution()
#S.accountsMerge(accounts)
print(S.accountsMerge(accounts))


