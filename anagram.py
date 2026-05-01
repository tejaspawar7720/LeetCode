class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        count2 = {}
        if len(s) != len(t):
            return False
        for char in s.lower():
            count[char] = count.get(char, 0) + 1
        for char in t.lower():
            count2[char] = count2.get(char, 0) + 1
    
        return count == count2
