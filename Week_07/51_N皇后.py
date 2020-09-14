class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pie, na = set(), set(), set()

        def backtrack(r):
            if r == n:
                process()
                return
            for c in range(n):
                if c in cols or r+c in pie or r-c in na:
                    continue
                # current level!!!!!
                cols.add(c)
                pie.add(r+c)
                na.add(r-c)
                tmp.append(c)
                backtrack(r+1)
                tmp.pop()
                na.remove(r-c)
                pie.remove(r+c)
                cols.remove(c)
                
        def process():
            res = []
            for i in tmp:
                x = ['.'] * i + ['Q'] + ['.'] * (n - 1 - i)
                res.append(''.join(x))
            ans.append(res)
            
        ans, tmp = [], []
        backtrack(0)
        return ans
