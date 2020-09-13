class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word):
        node = self.root
        for c in word:
            node.setdefault(c, {})
            node = node[c]
        node['#'] = True
        
    def remove(self, word):
        self._remove_node(self.root, word)

    def empty(self):
        return len(self.root) == 0

    def _remove_node(self, node, word):
        if not word and '#' in node and len(node) == 1:
            return 0
        if word and word[0] in node:
            children = self._remove_node(node[word[0]], word[1:])
            if children == 0:
                node.pop(word[0])
        return len(node)


class Solution:
    '''Trie树
    - 优化1：不用每次都从 Trie root 搜索整个单词，因为 DFS 已经有了搜索的能力，只需要判断下一个节点是否在当前 trie树的子树，因此 DFS 传入 current node，也得益于此，无需实现和调用 search；
    - 优化2：如果一个单词已经证明存在与board中，下一次检索就不用再检索，因为board 只能够可能有多种走法组成这个单词。也就是说，这个待检索的单词库是动态变化的。如果单词库为空，则无需再继续检索。
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []

        # 1. 用单词表，构建Trie树
        trie = Trie()
        for w in words: trie.insert(w)

        def DFS(i, j, path, cur):
            if '#' in cur:
                ans.add(path)
                trie.remove(path)
            c = board[i][j]
            board[i][j] = '.'
            for x, y in zip(dx, dy):
                if i+x < 0 or i+x >= m or j+y < 0 or j+y >= n or board[i+x][j+y] == '.':
                    continue
                if board[i+x][j+y] in cur:
                    DFS(i+x, j+y, path+board[i+x][j+y], cur[board[i+x][j+y]])
            board[i][j] = c
        
        # 2. 遍历board DFS
        ans, m, n = set(), len(board), len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(m):
            for j in range(n):
                if not trie.empty():
                    if board[i][j] in trie.root:
                        DFS(i, j, board[i][j], trie.root[board[i][j]])
                        
        return list(ans)