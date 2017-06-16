s1 = "pale"
s2 = "pales"
len_s1 = len(s1)
len_s2 = len(s2)

def count_errors(s2):
    j = 0
    error = 0
    for i in range(len(s2) - 1):
        if s2[i] == s1[j]:
            if j < len_s1:
                j = j + 1
        else:
            error = error + 1
            if j < len_s1:
                j = j + 1
    return error


if len_s1 - len_s2 > 1 or len_s1 - len_s2 < -1:
    print "false"
else:
    if (len_s2 <= len_s1):
        error = count_errors(s2)
    else:
        error = count_errors(s1)

    if error > 1:
        print "false"
    else:
        print "true"





