class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiouAEIOU"
        stack = []

        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])
        
        answer = ""

        for i in range(len(s)):
            if s[i] not in vowels:
                answer += (s[i])
            else:
                answer += (stack.pop())
        
        return answer
        