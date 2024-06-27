class Solution:
    def reverseWords(self, s: str) -> str:
        ans = reversed(s.split())
        return " ".join(ans)
        