class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        indegree = [0] * numCourses
        adj = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:

            indegree[course] += 1
            adj[prereq].append(course)
        

        queue = deque()
        
        for i in range(numCourses):

            if indegree[i] == 0:
                queue.append(i)
        

        completed = 0
        order = []

        while queue:

            course = queue.popleft()
            completed += 1
            order.append(course)

            for dependant in adj[course]:

                indegree[dependant] -= 1

                if indegree[dependant] == 0:

                    queue.append(dependant)

        print(list(reversed(order)))
        
        if completed == numCourses:
            return list(order)
        else:
            return []