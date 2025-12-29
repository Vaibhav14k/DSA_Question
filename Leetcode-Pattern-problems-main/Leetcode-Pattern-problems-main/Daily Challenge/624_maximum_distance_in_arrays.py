class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int: 
        n = len(arrays)
        res = 0
        current_min = arrays[0][0]
        current_max = arrays[0][-1]
        for i in range(1, n):
            res = max(res, abs(arrays[i][-1] - current_min), abs(arrays[i][0] - current_max))
            current_min = min(current_min, arrays[i][0])
            current_max = max(current_max, arrays[i][-1])
        return res
    '''def maxDistance(self, arrays: list[list[int]]) -> int: 
        n = len(arrays)
        maxx = []
        minn = []
        for i in arrays:
            maxx.append(i[-1])
            minn.append(i[0])
        # print(maxx,minn)
        res = 0
        for i in range(n):
            for j in range(n):
                diff = abs(maxx[j]-minn[i])
                if i != j and diff > res:
                    res = diff
        return res'''

obj = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
arrays = [[0,9],[1,7]]

print(obj.maxDistance(arrays))