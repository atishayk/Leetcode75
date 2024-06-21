from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        answer = []

        for i in range(len(candies)):
            if max < candies[i]:
                max = candies[i]

        for j in range(len(candies)):
            if candies[j] + extraCandies >= max:
                answer.append(True) 
            else:
                answer.append(False) 
        
        return answer

        


        