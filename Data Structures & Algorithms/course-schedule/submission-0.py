class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = {i : [] for i in range(numCourses)}

        for src, dst in prerequisites:

            indegree[dst] += 1
            adj[src].append(dst)
        

        queue = deque()
        
        for i in range(numCourses):

            if indegree[i] == 0:
                queue.append(i)
        
        completed = 0

        while queue:

            course = queue.popleft()
            completed += 1

            for dependant in adj[course]:

                indegree[dependant] -= 1

                if indegree[dependant] == 0:

                    queue.append(dependant)


        return completed == numCourses
