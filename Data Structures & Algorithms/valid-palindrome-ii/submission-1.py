class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if s == s[::-1]:
        #     return True

        # for i in range(len(s)):
        #     newS = s[:i] + s[i + 1:]
        #     if newS == newS[::-1]:
        #         return True
        # return False

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l + 1, r) or
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1
        return True

