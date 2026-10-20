from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Init: nodes are unique characters across all words
        # Using a set for neighbors prevents duplicate edges
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        # 2. Preprocess: Pairwise edge extraction
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Prefix trap: "apple" before "app" is invalid in any sorted dictionary
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Found first mismatch: w1[j] must come before w2[j]
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # 3. Process: Standard Kahn's Algorithm
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # 4. Return: Valid if every unique character was placed without a cycle
        return "".join(order) if len(order) == len(indegree) else ""