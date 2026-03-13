from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter(answers)
        rabbits = 0

        for answer in answers:
            if answer in dic:
                if answer + 1 < dic[answer]:
                    dic[answer] -= answer + 1
                else:
                    del dic[answer]

                rabbits += answer + 1

        return rabbits

        