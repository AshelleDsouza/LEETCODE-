
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        parents = defaultdict(list)
        queue = [beginWord]
        visited = {beginWord}
        found = False

        while queue and not found:
            next_level = set()

            for word in queue:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new = word[:i] + c + word[i+1:]

                        if new in words and new not in visited:
                            parents[new].append(word)
                            next_level.add(new)

                            if new == endWord:
                                found = True

            visited.update(next_level)
            queue = list(next_level)

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])

        return ans
