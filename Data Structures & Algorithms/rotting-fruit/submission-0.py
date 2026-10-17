class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        # we count sources in q and targets in fresh :

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # now we process till we have fresh and rots :
        while fresh > 0 and q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = r + dr, c + dc

                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1