def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    res = ""
    res_length = 0

    for i in range(len(s)):
        #even length
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > res_length:
                res = s[left:right+1]
                res_length = right - left + 1
            left -= 1
            right += 1

        # odd length
        left, right = i, i+1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > res_length:
                res = s[left:right+1]
                res_length = right - left + 1
            left -= 1
            right += 1

    return res

print(longest_palindromic_substring("babadar"))