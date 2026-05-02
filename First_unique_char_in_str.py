class Solution():
    def firstUniqChar(self, s):
        dics = {}
        for char in s:
            dics[char] = dics.get(char, 0) + 1

        for i in range(len(s)):
            if dics[s[i]] == 1:
                return i

        return "No uniqe ccharacter"
sl= Solution()
print(sl.firstUniqChar("lleettccoodde"))