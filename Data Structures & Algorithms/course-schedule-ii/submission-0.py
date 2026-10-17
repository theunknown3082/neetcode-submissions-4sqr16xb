class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            adj[preq].append(course)
            indegree[course] += 1

        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        order = []

        while q:
            curr = q.popleft()
            order.append(curr)

            for n in adj[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return order if len(order) == numCourses else []