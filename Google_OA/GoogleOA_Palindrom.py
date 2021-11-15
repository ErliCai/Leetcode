def palindrome(l):

    symmetric = dict()
    asymmetric  = dict()
    for s in l:
        if s[0] == s[1]:
            if s not in symmetric:
                symmetric[s] = 0
            symmetric[s] += 1
        else:
            if s not in asymmetric:
                asymmetric[s] = 0
            asymmetric[s] += 1

    rst = 0
    # print(symmetric, asymmetric)
    for s in asymmetric:
        s_reverse = s[1] + s[0]
        if s[1] + s[0] in asymmetric:
            length = min(asymmetric[s], asymmetric[s_reverse])
            asymmetric[s] -= length
            asymmetric[s_reverse] -= length
            rst += length * 4
    
    all_even = True
    for s in symmetric:
        if symmetric[s] % 2 != 0:
            all_even = False
        rst += (symmetric[s] // 2) * 4

    if not all_even:
        rst += 2
    return rst


test_case = ["ck", "kc", "ho", "kc"]
print(palindrome(test_case))

test_case2 = ["ck", "kc", "ho", "kc", "nn"]
print(palindrome(test_case2))
test_case2 = ["ck", "kc", "ho", "kc", "nn", "nn"]
print(palindrome(test_case2))
test_case2 = ["ab", "ba"]
print(palindrome(test_case2))