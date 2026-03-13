from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict()

        for bill in bills:
            if bill == 10:
                if dic[5] == 0:
                    return False
                else:
                    dic[5] -= 1

            elif bill == 20:
                temp = bill
                if dic[10] > 0:
                    dic[10] -= 1
                    temp -= 10

                num = temp // 5 - 1
                if dic[5] < num:
                    return False
                else:
                    dic[5] -= num 

            dic[bill] += 1


        return True
                
               
            







         
      
                

        