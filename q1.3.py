s1 = "a b c    "
length = len(s1)
for i in range(4,-1,-1):
    if (s1[i] is not " "):
        s1[length-1] = s1[i]
        length = length - 1
    else:
        s1[length-1] = "0"
        s1[length-2] = "2"
        s1[length-3] = "%"
        length = length - 3

print s1
