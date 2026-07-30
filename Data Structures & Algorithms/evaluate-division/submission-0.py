class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)

        for i in range(len(equations)):

            a, b, val = equations[i][0], equations[i][1], values[i]

            adj[a].append((b, val))
            adj[b].append((a, 1 / val))
        

        def bfs(c, d):

            if c not in adj or d not in adj:
                return -1

            queue = deque([(c, 1)])
            visited = set(c)

            while queue:

                var, val = queue.popleft()

                if var == d:
                    return val
                
                for neighbor, weight in adj[var]:

                    if neighbor not in visited:

                        queue.append((neighbor, val * weight))
                        visited.add(neighbor)
                
            return -1
        
        
        result = []
        
        for c, d in queries:

            result.append(bfs(c, d))
        
        return result