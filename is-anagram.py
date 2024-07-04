class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sval, tval = dict()

        #create dics for both strings counting characters
        for i in range(len(s)):
            sval[s[i]] = 1 + sval.get(s[i], 0)
            tval[t[i]] = 1 + tval.get(t[i], 0)
            
        for i in sval:
            if sval[i] != tval.get(i, 0):
                return False
        
        return True
            
        
        
            

        
        
    

