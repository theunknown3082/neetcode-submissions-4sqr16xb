class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        taken = 0

        while q:
            curr = q.popleft()
            taken += 1

            for n in adj[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return taken == numCourses