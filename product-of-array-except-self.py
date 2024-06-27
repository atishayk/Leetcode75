from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create two arrays to represent the product of the numbers to the
        # left and right of the current index

        '''
        [1, 3, 5, 2, 6, 7]
        for left, first index is always one as there is no number
        [1, 1, 3, 15, 30, 210]

        for right the opposite
        [540, 180, 84, 42, 7, 1]
        
        left = list(nums)
        right = list(nums)
        ans = []

        #left loop(ignoring the first index which is one)
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        #right, last value is 1
        right[len(nums) - 1] = 1
        for j in range(len(nums) - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        
        for k in range(len(nums)):
            ans.append(left[k] * right[k])

        return ans
        '''
        ans = list(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1] 
            ans[i] = ans[i] * prod
        
        return ans

        



        