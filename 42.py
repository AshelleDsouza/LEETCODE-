class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1

        return water