class Codec:
    def encode(self, strs):
        return ''.join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            i = j + int(s[i:j]) + 1
            strs.append(s[j+1:i])
        return strs

