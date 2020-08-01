#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """50%
        雨水的形成 -> 低洼 -> 左右边界        
        所谓“边界”，指的是当前位置往左数最高的柱子，和往右数最高的柱子

        恒定的真理：寻找重复性，消灭or减少重复计算的次数
        方法：空间换时间，升维
        """

        # # 1. 动态规划; 时间复杂度：O(n)，空间复杂度：O(n)
        # def dp():
        #     n, ans = len(height), 0
        #     left_to_right_max, right_to_left_max = [], []
        #     for i in range(0, n):
        #         if i == 0: left_to_right_max.append(height[i])
        #         left_to_right_max.append(max(height[i], left_to_right_max[-1]))
        #     for j in range(0, n):
        #         if j == 0: right_to_left_max.append(height[n-1-j])                    
        #         right_to_left_max = [max(height[n-1-j], right_to_left_max[0])] + right_to_left_max
        #     for k in range(0, n):
        #         min_val = min(left_to_right_max[k], right_to_left_max[k])
        #         ans += max(min_val-height[k], 0)
        #     return ans
        # return dp()


        # # 2. 单调递减栈; 时间复杂度：O(n)，空间复杂度：O(n)
        # # 栈只存储可能储水的柱子（有可能形成低洼的柱子）的坐标；
        # # 注意！！！存储的是坐标！！！为了计算距离！
        # def desc_stack():
        #     my_stack, ans = list(), 0
        #     for i in range(len(height)):
        #         while my_stack and height[i] > height[my_stack[-1]]:
        #             top = my_stack.pop()
        #             if not my_stack: break
        #             # 因为是单调递减栈，所以栈顶元素之前压入的元素一定比它大，且同时 height[i] 也比top大；
        #             # 如果栈顶元素弹出后，栈不为空，说明在top处会形成低洼；低洼的储水量由左右边界的较低高度决定。
        #             dist = i - my_stack[-1] - 1
        #             ht = min(height[my_stack[-1]], height[i]) - height[top]
        #             ans += ht * dist
        #         my_stack.append(i)
        #     return ans
        # return desc_stack()


        # 3. 双指针; 时间复杂度：O(n)，空间复杂度：O(1)
        # 心得：双指针从两端向中间逼近时，要搞清楚每种情况先移动哪个
        l, r, l_max, r_max, ans = 0, len(height)-1, 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < l_max:
                    # 此时 height[l] 的左右两侧各存在一个柱子高于它，而且左侧的柱子小于右侧
                    ans += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    ans += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return ans


# @lc code=end

