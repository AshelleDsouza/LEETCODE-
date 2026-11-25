
class Solution:
    def minLength(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1000000007, 1000000009
        base = 911382323

        def check(k):
            p1 = pow(base, k - 1, mod1)
            p2 = pow(base, k - 1, mod2)

            h1 = h2 = 0
            count = {}

            for i in range(n):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2

                if i >= k:
                    h1 = (h1 - nums[i-k] * p1) % mod1
                    h2 = (h2 - nums[i-k] * p2) % mod2

                if i >= k - 1:
                    key = (h1, h2)
                    count[key] = count.get(key, 0) + 1

            return any(v == 1 for v in count.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
