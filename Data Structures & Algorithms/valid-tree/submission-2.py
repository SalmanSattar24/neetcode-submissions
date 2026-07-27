class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. A valid tree MUST have exactly n - 1 edges.
        # If it doesn't, it either has a cycle or is disconnected.
        if len(edges) != n - 1:
            return False
            
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        # 2. Standard BFS just to verify all nodes are connected
        queue = deque([0])
        visited = {0}
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                # We only care about visiting new nodes. 
                # No parent tracking or cycle checking needed!
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        # 3. If we visited every node, it's a single connected component (and thus a tree)
        return len(visited) == n