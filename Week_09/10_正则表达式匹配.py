class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # way1: memo
        m, n, memo = len(s), len(p), dict() 
        def regmatch(i, j):
            if (i,j) in memo: 
                return memo[(i,j)]
            if i >= m and j >= n: res = True
            elif j >= n: res = False
            elif i >= m:
                if (n-j) % 2 == 1:
                    res = False
                else:
                    res = True
                    for k in range(j+1, n, 2):
                        if p[k] != '*':
                            res = False
            else:
                if j < n-1 and p[j+1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        res = regmatch(i+1, j) or regmatch(i, j+2)
                    else:
                        res = regmatch(i, j+2)
                else:
                    if s[i] == p[j] or p[j] == '.':
                        res = regmatch(i+1, j+1)
                    else:
                        res = False
            memo[(i,j)] = res
            return res
        return regmatch(0, 0)