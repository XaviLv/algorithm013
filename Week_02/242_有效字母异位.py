#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # 1. 排序 -》比较字符串是否相等，时间复杂度 O(NlogN)，空间复杂度 O(1)
        # return sorted(s) == sorted(t)

        # 2. hash表，统计字符出现的次数，遍历2次, 时间复杂度 O(N)，空间复杂度 O(N)
        if len(s) != len(t): return False
        if s == t: return True
        hash_map, hash_map2 = dict(), dict()
        for x in s:
            if x not in hash_map: hash_map[x] = 0
            hash_map[x] += 1
        for x in t:
            if x not in hash_map2: hash_map2[x] = 0
            hash_map2[x] += 1
        return hash_map == hash_map2

# @lc code=end

