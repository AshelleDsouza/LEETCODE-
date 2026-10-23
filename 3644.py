class Solution:
    def sortPermutation(self, nums):
        k = -1  # all bits set
        for i, x in enumerate(nums):
            if x != i:
                k &= x
        return 0 if k == -1 else k