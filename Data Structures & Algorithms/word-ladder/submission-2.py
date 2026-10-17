class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextword = word[:i] + c + word[i + 1:]
                    if nextword in wordSet and nextword not in visited:
                        visited.add(nextword)
                        q.append((nextword, step + 1))

        return 0