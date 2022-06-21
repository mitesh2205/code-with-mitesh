s = "()[]{}"
for i in range (len(s) - 1):
    if len(s) != 0:
        s = s.replace('()','').replace('{}','').replace('[]','')
print(len(s) == 0)