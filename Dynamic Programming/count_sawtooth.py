# this appeared in the GCA I took
# count the number of contiguous sawtooth subarrays of length >= 2
# DP problem -> dp[i] represents the number of contiguous sawtooth subarrays ENDING in arr[i]. 
def count_sawtooth(arr):
  up = 0
  down = 0
  count = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
      # up sawtooth ending in arr[i] = appending arr[i] to any contiguous down sawtooth ending in arr[i - 1] + the [arr[i - 1], arr[i]]
      up = down + 1
      # If we are in up sawtooth, then the number of down sawtooth should be reset (i.e. it is not possible to get a down sawtooth ending in arr[i])
      down = 0
      count += up
    elif arr[i] < arr[i - 1]:
      down = up + 1
      up = 0
      count += down
  return count
    
print(count_sawtooth([9, 8, 7, 6, 5])) # returns 4
print(count_sawtooth([10, 10, 10])) # returns 0
print(count_sawtooth([1, 2, 1, 2, 1])) # returns 10
print(count_sawtooth([1,2,1,3,4,-2])) # returns 9
arr5 = [-442024811,447425003,365210904,823944047,943356091,-781994958,872885721,-296856571,230380705,944396167,-636263320,-942060800,-116260950,-126531946,-838921202]
print(count_sawtooth(arr5)) # 31