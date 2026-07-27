class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) !=  n - 1:
            return False
        
        adj = {i : [] for i in range(n)}

        for n1, n2 in edges:
            
            adj[n1].append(n2)
            adj[n2].append(n1)


        queue = deque([0])
        visited = set([0])

        while queue:

            node = queue.popleft()

            for neighbor in adj[node]:

                if neighbor not in visited:

                    queue.append(neighbor)
                    visited.add(neighbor)
                

        
        return len(visited) == n