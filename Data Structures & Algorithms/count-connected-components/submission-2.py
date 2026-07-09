class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # normal DFS solution
        # similar problem: LC 547
        # adj = {i: [] for i in range(n)}
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)
            
        # visited = set()

        # def dfs(node, prev):
        #     if node in visited:
        #         return False
            
        #     visited.add(node)

        #     for nei in adj[node]:
        #         if nei == prev:
        #             continue
        #         if nei not in visited:
        #             dfs(nei, node)
            
        #     return True

        # counter = 0
        # for i in range(n):
        #     if i not in visited and dfs(i, -1):
        #         counter +=1
        
        # return counter

        # UnionFind solution
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res