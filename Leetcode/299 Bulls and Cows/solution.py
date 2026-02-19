from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic1 = Counter(secret)
        dic2 = Counter(guess)
        bulls = cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                dic1[secret[i]] -= 1
                dic2[guess[i]] -= 1

                if dic1[secret[i]] == 0:
                    del dic1[secret[i]]

                if dic2[guess[i]] == 0:
                    del dic2[guess[i]]

        for key in dic2:
            if key in dic1:
                cows += min(dic1[key], dic2[key])

        return f"{bulls}A{cows}B" 
         
