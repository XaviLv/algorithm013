class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash
        if len(s) != len(t):
            return False
        cache = [0] * 26
        a = ord('a')
        for c in s: cache[ord(c)-a] += 1
        for c in t:
            i = ord(c)-a
            if cache[i] == 0: 
                return False
            cache[i] -= 1
        return True

        # # sort
        # return sorted(s) == sorted(t)
