class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def backtrack(r, c, visited):
            visited.add((r, c))
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    backtrack(nr, nc, visited)
        for r in range(rows):
            backtrack(r, 0, pac)
            backtrack(r, cols - 1, atl)
        for c in range(cols):
            backtrack(0, c, pac)
            backtrack(rows - 1, c, atl)

        return [[r, c] for r, c in (pac & atl)] 