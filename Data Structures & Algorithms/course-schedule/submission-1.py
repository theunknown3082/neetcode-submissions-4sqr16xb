class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])


        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)

            for nei in adj[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)


        return len(order) == numCourses
            

            
        