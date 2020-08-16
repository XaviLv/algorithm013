#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # 光头哥神码 + 反向递归
        # if k == 0: return [[]]  # 返回值，配合下面的ans extend
        # ans = []
        # for i in range(k, n+1): # 题目要求从 1~n inclusive，所以这里右边界是 n+1
        #     ans.extend([m + [i] for m in self.combine(i-1, k-1)]) # 结果要接上 [i]
        # return ans

        # 超哥模板 + 正向递归
        ans = []
        def recursion(offset, comb):
            # termination
            if len(comb) == k:
                ans.append(comb)
                return
            # current level logic
            for i in range(offset, n+1):
                # drill down
                recursion(i+1, comb+[i])
        recursion(1, [])
        return ans


# @lc code=end

