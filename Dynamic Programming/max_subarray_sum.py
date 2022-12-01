class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_slice = 0
        max_sum = float('-inf')
        for num in nums:
            max_slice = max(num, max_slice + num)
            max_sum = max(max_sum, max_slice)
        return max_sum