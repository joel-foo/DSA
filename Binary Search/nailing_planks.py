# Time complexity: O((N + M) * log(M)) - prefix sum is computed in O(M), checking planks is O(N), total for one iteration is O(N + M). Binary search creates log(M) iterations, thus O((N + M) * log(M)).
# Question: https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/
def solution(A, B, C):
    M = len(C)
    lo = 1
    hi = M 
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        prefix_sum = [0] * (2 * M + 1)
        t = True
        for i in range(mid):
            prefix_sum[C[i]] += 1
        for i in range(1, 2 * M + 1):
            prefix_sum[i] += prefix_sum[i - 1]
        for i in range(len(A)):
            if prefix_sum[A[i] - 1] == prefix_sum[B[i]]:
                # means there is no nail between the these two ends, and thus need to expand search of all nails to the right
                t = False
                break
        if t:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

# Naive approach for checking results in high time complexity. i.e.:
# def check(end):
#     N = len(A)
#     count = 0
#     for i in range(N):
#         for j in range(end + 1):
#             if A[i] <= C[j] <= B[i]:
#                 count += 1
#                 break
#     return count
