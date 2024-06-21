'''
Different Orientations

01
10
010
101

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            elif flowerbed[0] == 1 and n <= 0:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n = n - 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
                    n = n - 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed [i + 1] == 0:
                    n = n - 1
                    flowerbed[i] = 1
        if n <= 0:
            return True
        else:
            return False


