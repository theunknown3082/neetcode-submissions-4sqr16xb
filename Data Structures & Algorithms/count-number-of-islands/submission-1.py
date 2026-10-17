class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def backtrack(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "0" and (r, c) not in visited:
                    backtrack(r, c)
                    islands += 1
        return islands