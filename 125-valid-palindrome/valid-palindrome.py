class Solution:
    def isPalindrome(self, s: str) -> bool:
        resultString = ''
        check = 0
        for char in s:
            if char.isalnum():
                resultString += char.lower()
        n = len(resultString)
        for i in range(n//2):
            if resultString[i] != resultString[n - i - 1]:
                return False
        return True