class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        rank = {i : 1 for i in range(n)}
        parent = {i : i for i in range(n)}

        def find(n):

            if n != parent[n]:

                parent[n] = find(parent[n])
            
            return parent[n]
        
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p2] > rank[p1]:

                parent[p1] = p2
                rank[p2] += rank[p1]
            
            else:

                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        

        for n1, n2 in edges:

            union(n1, n2)
        
        
        components = 0

        for n, p in parent.items():

            if n == p:
                components += 1
        
        return components