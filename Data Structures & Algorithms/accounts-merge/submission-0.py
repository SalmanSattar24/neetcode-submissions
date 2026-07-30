class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        rank = {i : 1 for i in range(n)}
        parent = {i : i for i in range(n)}


        def find(node):

            if node != parent[node]:

                parent[node] = find(parent[node])

            return parent[node]
        
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

        
        email_to_account = {}

        for i, account in enumerate(accounts):

            for email in account[1:]:

                if email in email_to_account:

                    union(i, email_to_account[email])
                
                else:

                    email_to_account[email] = i

        
        email_groups = defaultdict(list)

        for email, account in email_to_account.items():

            root = find(account)
            email_groups[root].append(email)
        
        
        result = []
        
        for account_id, emails in email_groups.items():

            name = accounts[account_id][0]
            result.append([name] + sorted(email_groups[account_id]))
        
        return result