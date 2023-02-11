def naming_a_company(ideas):
    groups = [set() for _ in range(len(ideas))]

    for idea in ideas:
        groups[ord(idea[0]) - ord('a')].add(idea[1:])
    res = 0
    for i in range(25):
        for j in range(i+1,26):
            mutuals = len(groups[i] & groups[j])
            res += 2 * (len(groups[i]) - mutuals) * (len(groups[j]) - mutuals)
    return res
    


