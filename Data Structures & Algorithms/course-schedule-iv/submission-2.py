class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = {i : [] for i in range(numCourses)}
        dependency_map = {i : set() for i in range(numCourses)}

        for prereq, course in prerequisites:

            adj[prereq].append(course)

        
        for course in range(numCourses):

            queue = deque([course])
            visited = set([course])

            while queue:

                current_course = queue.popleft()

                for neighbor in adj[current_course]:

                    if neighbor not in visited:

                        queue.append(neighbor)
                        visited.add(neighbor)
                        dependency_map[course].add(neighbor)
        
        # print(dependency_map)
        
        result = []
        for src, dst in queries:

            if dst in dependency_map[src]:
                result.append(True)
            
            else:
                result.append(False)
        
        return result