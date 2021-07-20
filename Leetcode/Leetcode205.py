def isIsomorphic(s, t):
    
    charset = set(s)
    translator = dict()
    for c in charset:
        p = s.index(c)
        translator[s[p]] = t[p]

    new_s = [translator[i] for i in s]
    new_s = "".join(new_s)

    return new_s == t and len(set(translator.keys())) == len(set(translator.values()))

print(isIsomorphic("badc", "baba"))

    
