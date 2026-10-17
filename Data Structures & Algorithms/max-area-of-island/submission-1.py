class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def backtrack(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            return 1 + backtrack(r + 1, c) + backtrack(r - 1, c) + backtrack(r, c + 1) + backtrack(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited:
                    maxArea = max(maxArea, backtrack(r, c))

        return maxArea
