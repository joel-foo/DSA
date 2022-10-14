class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        # this function is from house robber i
        def rob(l, r):
            a = 0 # dp[i - 2]
            b = 0 # dp[i - 1]
            for i in range(l, r):
                c = max(a + nums[i], b) 
                a = b;
                b = c; 
            return b 
        # Case 1 : rob house 1 to n - 1 (0 to n - 2)
        # Case 2 : rob house 2 to n (1 to n - 1)
        return max(rob(0, n - 1), rob(1, n))