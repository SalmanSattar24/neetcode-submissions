class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
        
        adj = {i : [] for i in range(n)}
        degree = [0] * n

        for u, v in edges:

            adj[u].append(v)
            adj[v].append(u)

            degree[u] += 1
            degree[v] += 1

        
        leaves_queue = deque()
        
        for i, deg in enumerate(degree):

            if deg == 1:
                leaves_queue.append(i)
        

        while leaves_queue:

            if n <= 2:
                return list(leaves_queue)
            
            for _ in range(len(leaves_queue)):

                leaf = leaves_queue.popleft()
                n -= 1

                for neighbor in adj[leaf]:

                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:

                        leaves_queue.append(neighbor)
