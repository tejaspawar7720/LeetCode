class Solution:
    def isValid(self, s):
        stack = []
        pare = {

            ')' : '(',
            '}' : '{',
            ']' : '['

        }
        for char in s:
            if char not in pare:
                stack.append(char)

            else:
                if not stack:
                    return False
                top = stack.pop()
                if pare[char] not in top:
                    return False
        return len(stack) == 0 



            
chr = Solution()
print(chr.isValid("{[()]}"))               
