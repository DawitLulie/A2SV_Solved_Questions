class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * 26
        
        for ch in s:
            i = ord(ch) - ord('a')
            
            new_count = (1 + sum(dp)) % MOD
            
            dp[i] = new_count
        
        return sum(dp) % MOD