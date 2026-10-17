class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        
        # we find the treasure count :

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # we perform operations :
        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 2147483647:
                        grid[row][col] = grid[r][c] + 1
                        q.append((row, col))

