class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) + 1
        rank = {i : 1 for i in range(1, n)}
        parent = {i : i for i in range(1, n)}

        def find(n):

            if n != parent[n]:

                parent[n] = find(parent[n])
            
            return parent[n]

        
        def union(u, v):

            pu, pv = find(u), find(v)

            if pu == pv:
                return False
            
            if rank[pv] > rank[pu]:

                parent[pu] = pv
                rank[pv] += rank[pu]
            
            else:

                parent[pv] = pu
                rank[pu] += rank[pv]
            
            return True
        

        for u, v in edges:

            if not union(u, v):
                return [u, v]