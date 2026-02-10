class Solution:
    def intToRoman(self, num: int) -> str:
        dic1 = {900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}
        dic2 = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        result = ""
        
        while num > 0:
            if (
                num in dic1 or 
                900 <= num < 1000 or 
                400 <= num < 500 or 
                90 <= num < 100 or 
                40 <= num < 50
                ):
             
                for key in dic1:
                    if num >= key:
                        result += dic1[key]
                        num -= key
                        break

            else:
                for key in dic2:
                    if num >= key:
                        result += dic2[key]
                        num -= key
                        break
        return result
        
                

