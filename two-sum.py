class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = set()
        answer = []

        for i in range(len(nums)):
            values.add(nums[i])
            if target - nums[i] in values:
                for j in range(len(nums)):
                    if nums[j] == target - nums[i] and j != i:
                        answer.append(i)
                        answer.append(j)
                        return answer

            