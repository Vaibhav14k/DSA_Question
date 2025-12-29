class Solution:
    def minOperations(self, logs: list[str]) -> int:
        if logs.count("../") >= len(logs) - logs.count("../"):
            return 0
        count = 0
        for i in logs:
            if i != "../" and i != "./":
                count +=1
            if i == "../":
                count -= 1
                count = max(0,count)
        return count

logs = ["d1/","d2/","../","d21/","./"]
logs = ["d1/","d2/","./","d3/","../","d31/"]
# logs = ["d1/","../","../","../"]
obj = Solution()
print(obj.minOperations(logs))