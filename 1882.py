import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []

        for t, task in enumerate(tasks):
            while busy and busy[0][0] <= t:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            if not free:
                end, w, i = heapq.heappop(busy)
                t = end
                heapq.heappush(free, (w, i))

                while busy and busy[0][0] <= t:
                    end, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (t + task, w, i))

        return ans