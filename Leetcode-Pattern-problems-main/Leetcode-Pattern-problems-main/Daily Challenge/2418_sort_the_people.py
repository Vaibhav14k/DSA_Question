class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        data = []
        for i in range(len(names)):
            data.append((names[i],heights[i]))
        data.sort(key=lambda x:x[1],reverse=True)
        return [x[0] for x in data]

obj = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(obj.sortPeople(names,heights))