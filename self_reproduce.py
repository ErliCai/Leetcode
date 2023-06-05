l = ['s = "".join(l[:-1])', '\n', 'print("l = "+ l.__str__())', '\n', 'print(s)', '\n']

s = "".join(l[:-1])
print("l = "+ l.__str__() + "\n")
print(s)