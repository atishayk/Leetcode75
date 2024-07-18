from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
      a = 0
      b = len(numbers) - 1

      while (numbers[a] + numbers[b] != target):
        if target - numbers[a] < numbers[b]:
            b -= 1
        if target - numbers[a] > numbers[b]:
            a += 1
      

      answer = [a + 1, b + 1]
      return answer
      

        