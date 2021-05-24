import numpy as np

def soundex(string):
    tmp = ""
    for s in string:
        if s >= "a" and s <= "z":
            tmp += s
    string = tmp
    
    if len(string) == 0 or len(string) > 15:
        return ""
    ans = string[0]
    for s in string[1:]:
        if s in "aeiouhwy":
            digit = "0"
        elif s in "bfpy":
            digit = "1"
        elif s in "cgjkqsxz":
            digit = "2"
        elif s in "dt":
            digit = "3"
        elif s in "l":
            digit = "4"
        elif s in "mn":
            digit = "5"
        elif s in "r":
            digit = "6"
        else:
            continue
        if ans[-1] != digit:
            ans += digit
    ans = ans.replace("0","")
    if len(ans) > 4:
        ans = ans[0:4]
    elif len(ans) < 4:
        ans = ans + "0" * (4 - len(ans))
    return ans

def edit_dist(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    
    if len1 > 10 or len2 > 10:
        return 10
    
    dp = np.zeros((len1 + 1,len2 + 1),dtype=np.int8)
    for i in range(len1 + 1):
        dp[i][0] = i    
    for j in range(len2 + 1):
        dp[0][j] = j
     
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
    return dp[len1][len2]
