# 1D DP - Time: O(n), Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]
  
# O(1) DP - Time: O(n), Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0 # dp[i - 2]
        b = 0 # dp[i - 1]
        for num in nums:
            c = max(a + num, b) # calculates i
            a = b; # i-2 := i-1
            b = c; # i-1 := i
        return b