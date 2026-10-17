class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, n):
            nonlocal components
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            components -= 1
            return True
        for u, v in edges:
            union(u, v, n)
        
        return components