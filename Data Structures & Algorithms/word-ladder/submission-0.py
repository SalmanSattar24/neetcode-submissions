class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):

                pattern = word[: i] + '*' + word[i + 1 :]
                adj[pattern].append(word)

        print(adj)
        
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:

            w, l = queue.popleft()
            
            if w == endWord:
                return l

            for i in range(len(w)):

                pattern = w[: i] + '*' + w[i + 1 :]

                for neighbor in adj[pattern]:
                    
                    if neighbor not in visited:

                        queue.append((neighbor, l + 1))
                        visited.add(neighbor)
        
        return 0