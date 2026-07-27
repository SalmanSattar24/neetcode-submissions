class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        adj = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:

            indegree[course] += 1
            adj[prereq].append(course)

        
        queue = deque()
        for course in range(numCourses):

            if indegree[course] == 0:
                queue.append(course)
        

        completed = 0
        sequence = []

        while queue:

            course = queue.popleft()
            completed += 1
            sequence.append(course)

            for dependants in adj[course]:

                indegree[dependants] -= 1

                if indegree[dependants] == 0:

                    queue.append(dependants)
        

        if completed == numCourses:
            return sequence
        
        else:
            return []