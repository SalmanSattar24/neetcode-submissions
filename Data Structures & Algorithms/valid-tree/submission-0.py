class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
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
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

            