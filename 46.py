class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)

        def backtrack(start):
            if start == n:
                res.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res