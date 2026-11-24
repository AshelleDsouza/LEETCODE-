
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = [(beginWord, 1)]
        visited = {beginWord}

        while queue:
            word, steps = queue.pop(0)

            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = word[:i] + c + word[i+1:]

                    if new in words and new not in visited:
                        visited.add(new)
                        queue.append((new, steps + 1))

        return 0
