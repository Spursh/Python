s1 = "Tact Coa"
s2 = "atco cta"
asd = 0
if len(s1) == len(s2):
    sort_s1 = sorted(s1.lower())
    sort_s2 = sorted(s2.lower())
    if (sort_s1 == sort_s2):
        i = 0
        length = len(s2)-1
        while i < length:
            if s2[i] == s2[length]:
                i = i + 1
                length = length - 1
            elif s2[i] != s2[length] and (s2[length] == " " or s2[i] == " "):
                i = i+1
                length = length - 1
            else:
                asd = 1;
    else:
        asd = 1
if asd == 0:
    print "pali perm"
else:
    print "not pali"
