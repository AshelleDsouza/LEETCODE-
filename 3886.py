from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True
            prev_max = float('-inf')

            for i in range(0, n, k):
                arr = nums[i:i + k]
                m = len(arr)

                drops = 0
                drop_idx = -1

                for j in range(m):
                    if arr[j] > arr[(j + 1) % m]:
                        drops += 1
                        drop_idx = j

                if drops > 1:
                    possible = False
                    break

                if drops == 1:
                    rotated = arr[drop_idx + 1:] + arr[:drop_idx + 1]
                else:
                    rotated = arr

                if rotated[0] < prev_max:
                    possible = False
                    break

                prev_max = rotated[-1]

            if possible:
                ans += k

        return ans