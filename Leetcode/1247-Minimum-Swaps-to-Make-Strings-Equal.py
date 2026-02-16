class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = y = 0
        
        for a, b in zip(s1, s2):
            if a != b:
                x += a == "x"
                y += a == "y"
        
        if (x + y) % 2:
            return -1
        
        return (x + 1)//2 + (y + 1)//2
