class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp = ""
        arr = []
        for i in s:
            if i == "(" :
                arr.append(temp)
                temp = ""
            elif i == ")":
                temp = temp [::-1]
                temp = arr.pop() + temp
            else:
                temp += i
        return temp

obj = Solution()
s = "(abcd)"
s = "(ed(et(oc))el)"
# s = "(u(love)i)"
print(obj.reverseParentheses(s))