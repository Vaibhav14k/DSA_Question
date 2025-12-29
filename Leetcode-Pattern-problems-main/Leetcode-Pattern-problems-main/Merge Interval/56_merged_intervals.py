class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        if n==0:
            return []
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        merged = [intervals[0]]
        
        for i in intervals[1:]:
            last = merged[-1]
            if last[1]>=i[0]:
                last[1]= max(i[1],last[1])
            else:
                merged.append(i)
        print(merged)
        return merged


obj = Solution()
intervals = [[1,3],[2,6],[15,18],[8,10]]
intervals = [[1,4],[4,5]]
print(obj.merge(intervals))