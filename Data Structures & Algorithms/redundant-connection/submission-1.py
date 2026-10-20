class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return False

            if rank[rootx] < rank[rooty]:
                rootx, rooty = rooty, rootx
            parent[rootx] = rooty
            
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []