class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for c in s:
            if c.isalnum():
                clean_string += c.lower()

        return clean_string == clean_string[::-1]