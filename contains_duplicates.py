class Solution(object):
    def containsDuplicate(self, nums):
       stack = {}
       for num in nums:
           stack[num] = stack.get(num, 0) + 1
       for i in range(len(nums)):
           if stack[nums[i]] != 1:
               return True
       return False    
        
           


                       
           


