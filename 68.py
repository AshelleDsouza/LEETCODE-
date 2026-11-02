class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            line = []
            letters = 0

            while i < len(words) and letters + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                letters += len(words[i])
                i += 1

            if i == len(words) or len(line) == 1:
                line_text = " ".join(line)
                result.append(line_text + " " * (maxWidth - len(line_text)))
            else:
                spaces = maxWidth - letters
                gaps = len(line) - 1

                space_each = spaces // gaps
                extra = spaces % gaps

                line_text = ""

                for j in range(gaps):
                    line_text += line[j]
                    line_text += " " * (space_each + (1 if j < extra else 0))

                line_text += line[-1]
                result.append(line_text)

        return result