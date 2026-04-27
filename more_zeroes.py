class Solution(object):
    def moveZeroes(self, nums):
        k  = 0  
        for i in range(len(nums)):
            nums[i] = 0
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        return k