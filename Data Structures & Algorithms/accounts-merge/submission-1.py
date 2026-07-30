class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # 'n' represents the total number of accounts we are given initially.
        n = len(accounts)
        
        # Initialize Union-Find structures. 
        # We use the index of the account (0 to n-1) to represent each account group.
        # 'rank' keeps track of the size/depth of the tree to keep it balanced during union.
        rank = {i : 1 for i in range(n)}
        # 'parent' maps each account index to its parent. Initially, every account is its own parent.
        parent = {i : i for i in range(n)}

        # Helper function 1: Find the root parent of a given node (account index).
        def find(node):
            # If the node is not its own parent, we haven't found the root yet.
            if node != parent[node]:
                # Recursively find the root and update the parent pointer directly to the root.
                # This is called 'Path Compression' and speeds up future lookups.
                parent[node] = find(parent[node])
            # Return the ultimate root node.
            return parent[node]
        
        # Helper function 2: Merge two sets (account indices) together.
        def union(u, v):
            # Find the root parents of both nodes.
            pu, pv = find(u), find(v)

            # If they already have the same root, they are already connected. No need to merge.
            if pu == pv:
                return False
            
            # Union by Rank: Attach the smaller tree under the root of the larger tree.
            # This helps keep the overall tree flat, ensuring operations remain near O(1) time.
            if rank[pv] > rank[pu]:
                parent[pu] = pv
                rank[pv] += rank[pu]
            else:
                parent[pv] = pu
                rank[pu] += rank[pv]

            # Return True to indicate a successful merge.
            return True

        
        # This dictionary will map each unique email string to an account index.
        # Format: { "email@example.com" : account_index }
        email_to_account = {}

        # --- STEP 1: Process accounts and build the Union-Find graph ---
        for i, account in enumerate(accounts):
            # Iterate through all emails in the current account (skipping the name at index 0).
            for email in account[1:]:
                # If we've seen this email before, it means the current account (i) 
                # and the account that previously claimed this email belong to the same person.
                if email in email_to_account:
                    # Merge the two account groups together.
                    union(i, email_to_account[email])
                else:
                    # If it's a new email, record that it belongs to the current account index (i).
                    email_to_account[email] = i

        
        # --- STEP 2: Group emails by their ultimate root account ---
        # defaultdict(list) allows us to easily append to lists without checking if the key exists.
        email_groups = defaultdict(list)

        for email, account in email_to_account.items():
            # For every unique email, find the ultimate root account ID it belongs to.
            # (Because some accounts were merged, the original 'account' might not be the root anymore).
            root = find(account)
            # Add the email to the group belonging to the root account.
            email_groups[root].append(email)
        
        
        # --- STEP 3: Format the final result ---
        result = []
        
        for account_id, emails in email_groups.items():
            # Grab the name from the original accounts list using the root account_id.
            name = accounts[account_id][0]
            
            # The problem requires the emails to be sorted in lexicographical (alphabetical) order.
            # We construct the final array for this person: [Name, email1, email2, ...]
            # Note: email_groups[account_id] is the same as the 'emails' variable in this loop.
            result.append([name] + sorted(emails))
        
        return result