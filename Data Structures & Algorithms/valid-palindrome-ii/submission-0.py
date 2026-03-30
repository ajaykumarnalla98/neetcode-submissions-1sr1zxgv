class Solution:
    def validPalindrome(self, s: str) -> bool:
        # newStr = ''

        # for c in s:
        #     newStr += c.lower()
        #     if s == newStr:
        #         return True
        # return False

        if s == s[::-1]:
            return True

        for i in range(len(s)):
            newS = s[:i] + s[i + 1:]
            if newS == newS[::-1]:
                return True
        return False