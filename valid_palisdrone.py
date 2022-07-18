s = "A man, a plan, a canal: Panama"
s = (''.join(ch for ch in s if ch.isalnum())).lower()
if s == s[::-1]:
    print(True)