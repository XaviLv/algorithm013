from collections import deque

class Solution:

    def get_mask(self, word):
        res = []
        for i in range(len(word)):
            res.append(word[:i] + '*' + word[i+1:])
        return res

    def init_adjacent(self, wordList):
        adj_dict = dict()
        for word in wordList:
            for key in self.get_mask(word):
                if key not in adj_dict:
                    adj_dict[key] = set()
                adj_dict[key].add(word)
        return adj_dict

    def move(self, visited, queue, other_visited):
        word, step = queue.popleft()
        mask = self.get_mask(word)
        for m in mask:
            if m in self.adj_dict:
                for w in self.adj_dict[m]:
                    if w in other_visited:
                        return other_visited[w] + step
                    if w not in visited:
                        visited[w] = 1 + step
                        queue.append((w, 1 + step))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        self.adj_dict = self.init_adjacent(wordList)
        queue_a, queue_b, visited_a, visited_b = deque(), deque(), dict(), dict()
        queue_a.append((beginWord, 1))
        queue_b.append((endWord, 1))
        visited_b[endWord] = 1
        ans = 0
        while queue_a and queue_b:
            # move left
            ans = self.move(visited_a, queue_a, visited_b)

            # move right
            if ans == 0:
                ans = self.move(visited_b, queue_b, visited_a)

            if ans:
                return ans
        
        return 0


sol = Solution()
test_cases = [
    ['hit', 'cog', ["hot","dot","dog","lot","log","cog"]],
    ['hit', 'cog', ["hot","dot","dog","lot","log"]],
    ['a', 'c', ['a', 'b', 'c']]
]

for case in test_cases:
    print(case, sol.ladderLength(case[0], case[1], case[2]))