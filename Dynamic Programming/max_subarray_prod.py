#O(n) Time, O(1) space - 1D DP
# Key idea: prevMin becomes prevMax when num < 0, else prevMax becomes prevMin when num > 0
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMin = prevMax = res = nums[0]
        for i in range(1, len(nums)):
            x = prevMin * nums[i]
            y = prevMax * nums[i]
            prevMin = min(x, y, nums[i])
            prevMax = max(x, y, nums[i])
            res = max(res, prevMax)
        return res
    

#O(n3) brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        ans = nums[0]
        for i in range(N):
            for j in range(i + 1, N):
                n = nums[i]
                for k in range(i + 1, j + 1):
                    n *= nums[k]
                ans = max(n, ans)
        return ans

# O(n2) optimised brute force method
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        ans = nums[0]
        for i in range(N):
            k = nums[i]
            for j in range(i + 1, N):
                k *= nums[j]
                ans = max(k, ans)
        return ans


