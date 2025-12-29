from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [defaultdict(int)]
        i = 0
        while i < N:
            print(stack)
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                i_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                top = stack.pop()
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][name] += multiplicity
        counts = stack[0]
        return ''.join(name + (str(counts[name]) if counts[name] > 1 else '')
                        for name in sorted(counts))

solution = Solution()
print(solution.countOfAtoms("Mg(OH)2")) 
