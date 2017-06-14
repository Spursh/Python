s1 = "abcad"
s2 = ""
for i in s1:
    if i not in s2:
        s2 = s2+i
    else:
        print "not unique"
        break;
