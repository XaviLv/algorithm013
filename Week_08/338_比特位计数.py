class Solution:
    def countBits(self, num: int) -> List[int]:
        # way1: 时间复杂度O(n)，因为 x & (x-1) 的意思是清零 x 最低位的 1，
        # 而 ans[i] 的意思是数字 i 二进制表示内 1 的个数，所以 ans[x] 和 ans[x&(x-1)] 的二进制数内 1 的个数相差 1 个
        ans = [0] * (num + 1)
        for x in range(1, num + 1):
            ans[x] = ans[x & (x-1)] + 1
        return ans
        
        # # way2: O(n * k), k 表示 1 的平均个数
        # ans = []
        # for x in range(num + 1):
        #     t = 0
        #     while x:
        #         p = x & -x
        #         x = x & (x - 1)
        #         t += 1
        #     ans.append(t)
        # return ans