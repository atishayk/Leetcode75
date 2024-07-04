class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newstr = ""
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        
        ptr1 = 0
        ptr2 = len(newstr) - 1

        while(ptr1 <= ptr2):
            if newstr[ptr1] != newstr[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True
            
        