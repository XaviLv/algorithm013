#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """因为bills里的元素都是整除关系，所以可以直接利用贪心算法求解。
        找钱时，每次都优先使用最大的钱。

        如果对 list 使用 remove，会有 O(N) 的元素搬移开销，可以使用元素计数
        """
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif b == 20:
                if five >= 1 and ten >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
      
# @lc code=end
