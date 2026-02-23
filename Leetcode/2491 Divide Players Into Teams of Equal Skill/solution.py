class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        # If odd number of players, cannot pair everyone
        if n % 2 != 0:
            return -1

        skill.sort()  
        left, right = 0, n - 1
        chemistry = 0
        target_sum = skill[left] + skill[right]  

        while left < right:
            current_sum = skill[left] + skill[right]

            if current_sum != target_sum:
                return -1

            chemistry += skill[left] * skill[right]  
            left += 1
            right -= 1

        return chemistry