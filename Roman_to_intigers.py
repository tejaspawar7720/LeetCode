class Solution:
    def roman_to_int(self,romanstring):
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        result = 0

        for i in range(len(romanstring)):
            current = roman[romanstring[i]]

            if i+1 < len(romanstring):
                next_val = roman[romanstring[i+1]]

                if current < next_val:
                    result -= current

                else:
                    result += current

            else:
                result += current

        return result

rm=Solution()
print(rm.roman_to_int("LVIII"))

            