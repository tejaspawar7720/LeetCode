class Solution(object):
    def majorityElement(self, nums):
       dic = {}
       for num in nums:
           dic[num] = dic.get(num, 0 ) + 1
        
       for i in range(len(nums)):
           if dic[nums[i]] > len(nums) / 2:
               return nums[i]
       return -1   