def solution(S):
    # write your code in Python 3.6
    n = len(S)
    S = list(S)
    res = ""
    # Base case
    if S[0] != "?" and S[n-1] != "?":
        if S[0] != S[n-1]:
            return "NO"

    for i in range(n):
        for j in range(n-(i+1),-1,-1):
            if S[i] == "?" and S[j] == "?":
                S[i] = "a"
                S[j] = "a"
                break
            elif S[i] == S[j]:
                break
            elif S[i] == "?":
                S[i] = S[j]
                break
            elif S[j] == "?":
                S[j] = S[i]
                break

    return res.join(S)

print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))
print(solution("??????"))
print(solution("ab??ba"))
print(solution("ab??ba??aba"))
