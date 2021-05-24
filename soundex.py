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
