class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pre = [0]
        for d in days:
            pre.append(pre[-1] + d)

        def toDay(s):
            m, d = int(s[:2]), int(s[3:])
            return pre[m - 1] + d

        start = max(toDay(arriveAlice), toDay(arriveBob))
        end = min(toDay(leaveAlice), toDay(leaveBob))
        return max(0, end - start + 1)