def  maxTime(s):
    digits = [s[0], s[1], s[3], s[4]]

    rst = [i if i != "?" else None for i in digits]
    if digits[0] == "?":
        if digits[1] == "?" or (int(digits[1]) <= 3):
            rst[0] = "2"
        else:
            rst[0] = "1"

    if digits[1] == "?":
        if int(rst[0]) == 2:
            rst[1] = "3"
        else:
            rst[1] = "9"

    if digits[2] == "?":
        rst[2] = "5"

    if digits[3] == "?":
        rst[3] = "9"
        

    rst = rst[0] + rst[1] + ":" + rst[2] + rst[3]
    return rst


print(maxTime("23:5?"))
print(maxTime("??:??"))
print(maxTime("2?:22"))
print(maxTime("1?:??"))
print(maxTime("22:22"))