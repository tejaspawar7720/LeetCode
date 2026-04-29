class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, len(nums)):
            nums[i] =0

# class Solution:
#     def moveZeroes(self, nums):
#         res = []
#         count = 0
#         for i in range(len(nums)):
#                 if nums[i] != 0:                        my solution, but it is not in place, so it is not accepted by leetcode but output is correct
#                     res.append(nums[i])
#                 elif nums[i] == 0:
#                     count += 1
#         for j in range(count):
#                         res.append(0)
#         return res
    
# sl = Solution()
# print(sl.moveZeroes([0,1,0,12,3]))