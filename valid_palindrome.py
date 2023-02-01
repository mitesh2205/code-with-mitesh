def valid_palindrome(s):
    s = s.lower()
    i = 0
    j = len(s) - 1

    while i < j:    
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return is_palindrome(s, i + 1, j) or is_palindrome(s, i, j - 1)

    return True

def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True