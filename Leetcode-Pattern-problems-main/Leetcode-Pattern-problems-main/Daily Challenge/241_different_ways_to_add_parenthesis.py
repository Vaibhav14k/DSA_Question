class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        def backtract(left,right):
            res = []
            for i in range(left,right+1):
                op = expression[i]
                if op in operations:
                    left_val = backtract(left,i-1)
                    right_val = backtract(i+1,right)
                    for i in left_val:
                        for j in right_val:
                            res.append(operations[op](i,j))
            if not res:
                res.append(int(expression[left:right+1]))
            return res
        return backtract(0,len(expression)-1)

obj = Solution()
print(obj.diffWaysToCompute("2-1-1"))  # Output: [0,2]