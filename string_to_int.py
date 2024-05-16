def string_to_int(s):
    if s == "":
        return -1
    
    value = 0
    for i in range(len(s)-1, -1, -1):
        if not s[i].isdigit():
            return -1
        print(value)
        value += (ord(s[i]) - ord('0')) * 10**(len(s)-1-i)

    return value


print(string_to_int("1234")) # 1234