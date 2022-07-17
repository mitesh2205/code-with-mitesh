s= "a"
t= "ab"
if len(s) == len(t) and set(s) == set(t):
    for i in range (len(s)):
        if s[i] in t and t[i] in s:
            print(s.count(s[i]) == t.count(s[i]))
        else:
            print(False)