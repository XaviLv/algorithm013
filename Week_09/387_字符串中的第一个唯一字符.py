class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        cache = dict()
        for c in s:
            cache[c] = cache.get(c, 0) + 1
        for i, c in enumerate(s):
            if cache[c] == 1:
                return i
        return -1