class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, min(i + r, len(nums))):
                total += nums[j]

                if l <= j - i + 1 <= r and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1