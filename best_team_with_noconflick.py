def best_team_with_noconflict(scores,ages):
    if len(scores) == 0:
        return 0

    for i in range(len(ages)):
        for j in range(i+1,len(ages)):
            if ages[i] > ages[j]:
                ages[i],ages[j] = ages[j],ages[i]
                scores[i],scores[j] = scores[j],scores[i]
            elif ages[i] == ages[j] and scores[i] > scores[j]:
                scores[i],scores[j] = scores[j],scores[i]

    dp = [0] * len(scores)

    result = dp[0] = scores[0]

    for i in range(1,len(scores)):
        dp[i] = scores[i]
        for j in range(i):
            if scores[j] >= scores[i]:
                dp[i] = max(dp[i],dp[j]+scores[i])
        result = max(result,dp[i])

    return result