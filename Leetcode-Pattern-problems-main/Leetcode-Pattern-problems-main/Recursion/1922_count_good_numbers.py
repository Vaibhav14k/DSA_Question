class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def mod_exp(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        
        if n == 1:
            return 5
        
        temp1 = n // 2 + n % 2
        temp2 = n // 2
        
        result = (mod_exp(4, temp2, MOD) * mod_exp(5, temp1, MOD)) % MOD
        
        return result


obj = Solution()
print(obj.countGoodNumbers(50))