class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        count=0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        merged = [intervals[0]]
        for i in intervals[1:]:
            last = merged[-1]
            if last[1]>i[0]:
                count+=1    
            else:
                merged.append(i)
        print(count)
        return count

obj = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
intervals = [[1,100],[11,22],[1,11],[2,12]]
obj.eraseOverlapIntervals(intervals)