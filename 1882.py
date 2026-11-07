import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end, w, s = heapq.heappop(busy)
                heapq.heappush(free, (w, s))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, w, s = heapq.heappop(busy)
                    heapq.heappush(free, (w, s))

            w, s = heapq.heappop(free)
            ans.append(s)
            heapq.heappush(busy, (time + task, w, s))

        return ans