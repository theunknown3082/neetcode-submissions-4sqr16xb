class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        size = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return False
            
            if size[rootx] < size[rooty]:
                rootx, rooty = rooty, rootx

            parent[rooty] = rootx
            size[rootx] += size[rooty]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []            
            