from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # checks if GCD even exists
        smaller = ""
        if (str1 + str2 != str2 + str1):
            return ""
        else:
            if len(str1) < len(str2):
                smaller = str1
            else:
                smaller = str2
            size = gcd(len(str1), len(str2))
            return smaller[0:size]



            



