from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            if k == 1:
                if nums == sorted(nums):
                    ans += 1
                continue

            valid = True

            for i in range(0, n, k):
                arr = nums[i:i + k]
                drops = sum(
                    arr[j] > arr[(j + 1) % k]
                    for j in range(k)
                )

                if drops > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans