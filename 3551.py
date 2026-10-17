class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each number with its (digit_sum, value) and its original index
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((get_digit_sum(num), num, i))
        
        # Sort based on digit sum, then by value
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        
        # Find the minimum swaps to sort the array using cycle detection
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps