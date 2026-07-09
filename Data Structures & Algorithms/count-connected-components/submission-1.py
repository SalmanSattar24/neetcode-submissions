class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if nei not in visited:
                    dfs(nei, node)
            
            return True

        counter = 0
        for i in range(n):
            if i not in visited and dfs(i, -1):
                counter +=1
        
        return counter