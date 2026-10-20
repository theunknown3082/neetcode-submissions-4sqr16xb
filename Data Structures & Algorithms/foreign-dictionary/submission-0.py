from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Init: standard 26-size arrays
        adj = [[] for _ in range(26)]
        indegree = [0] * 26
        exists = [False] * 26

        # Mark which characters actually exist in the words
        for w in words:
            for c in w:
                exists[ord(c) - ord('a')] = True

        total_unique = sum(exists)

        # 2. Preprocess: Pairwise edge extraction
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Prefix trap: "apple" before "app" is invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    u = ord(w1[j]) - ord('a')
                    v = ord(w2[j]) - ord('a')
                    
                    # Add edge u -> v (avoid duplicate edges if already present)
                    if v not in adj[u]:
                        adj[u].append(v)
                        indegree[v] += 1
                    break

        # 3. Process: Standard Kahn's queue
        queue = deque([i for i in range(26) if exists[i] and indegree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(chr(node + ord('a')))

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # 4. Return: Check if all unique characters were ordered (cycle detection)
        return "".join(order) if len(order) == total_unique else ""