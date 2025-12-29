import re,math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        common_divisor = math.gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"

solution = Solution()
result = solution.fractionAddition("-1/2+1/2+1/3")
print(result)  # Output should be "1/3"
