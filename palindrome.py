class Solution:
    def validPalindrome(self, s):
        def check_palindrome(s, i, j):
            while i < j:
                # print(s[i])
                # print(s[j])
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # print("Hi")
                return check_palindrome(s, i, j-1) or check_palindrome(s, i+1, j)
            i += 1
            j -= 1
        # print("Hello")
        return True


obj = Solution()
print(obj.validPalindrome("abcdkddcba"))
