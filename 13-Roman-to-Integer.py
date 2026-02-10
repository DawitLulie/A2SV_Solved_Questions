class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = i = 0
         
        while i < len(s):
            if i + 1 < len(s):
                if s[i] == "C" and s[i+1] == "M":
                    result += 900
                    i += 1

                elif s[i] == "C" and  s[i+1] == "D":
                    result += 400
                    i += 1

                elif s[i] == "X" and s[i+1] == "C":
                    result += 90
                    i += 1

                elif s[i] == "X" and s[i+1] == "L":
                    result += 40
                    i += 1

                elif s[i] == "I" and s[i+1] == "X":
                    result += 9
                    i += 1

                elif s[i] == "I" and s[i+1] == "V":
                    result += 4
                    i += 1
                
                else:
                    result += dic[s[i]]
  
            else:
                result += dic[s[i]]

            i += 1

        return result


        
        
        