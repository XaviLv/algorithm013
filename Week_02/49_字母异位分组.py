#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        mem = dict()
        for i, word in enumerate(strs):
            t = ''.join(sorted(word))
            if t not in mem:
                mem[t] = []
            mem[t].append(word)
        return [v for v in mem.values()]
# @lc code=end

