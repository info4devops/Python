#Q: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example: Input: nums = [2,7,11,15], target = 9 ==> Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#---------------------------------------------------------------------------------

nums = [2,7,11,15]
target = 9
for i in range(len(nums)-1):
  for j in range(i+1,len(nums)):
    if nums[i]+nums[j]== target:
      print([i,j])
    