class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                cleaned += char
        return cleaned[::-1].lower() == cleaned.lower()
    