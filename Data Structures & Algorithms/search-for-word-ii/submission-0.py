class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            curr = root
            for ch in w:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = w
        
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return
            
            nextnode = node.children[ch]

            if nextnode.word:
                res.append(nextnode.word)
                nextnode.word = None
            
            board[r][c] = "#"

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nextnode)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res