from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n, m, w = len(s), len(words), len(words[0])
        if m * w > n:
            return []

        need = Counter(words)
        res = []

        for off in range(w):
            left = off
            count = 0
            seen = Counter()

            for right in range(off, n - w + 1, w):
                word = s[right:right + w]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        seen[s[left:left + w]] -= 1
                        left += w
                        count -= 1

                    if count == m:
                        res.append(left)
                        seen[s[left:left + w]] -= 1
                        left += w
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + w

        return res