s1 = "abc"
s2 = "cab"
s3 = s2 * 2
if (len(s2) == len(s1) and s3.__contains__(s1)):
    print "permutaion string"
else:
    print "non permutaion string"