class Solution(object):
    def isIsomorphic(self, s, t):
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in dic1:
                if dic1[char_s] != char_t:
                    return False
            else:
                dic1[char_s] = char_t              
            
            if char_t in dic2:
                if dic2[char_t] != char_s:
                    return False
            else:
                dic2[char_t] = char_s

        return True