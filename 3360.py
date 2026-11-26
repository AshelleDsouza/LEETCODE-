
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        turn = 0

        while n >= stones:
            n -= stones
            stones -= 1
            turn += 1

        return turn % 2 == 1
