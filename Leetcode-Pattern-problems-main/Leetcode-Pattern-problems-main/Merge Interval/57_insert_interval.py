class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not newInterval:
            return intervals
        n=len(intervals)
        merged = []
        i = 0
        # Handle Non overlapping
        while i<n and intervals[i][1]<newInterval[0]:
            merged.append(intervals[i])
            i+=1
        print(merged)
        # Handle Overlapping and merge all
        while (i<n and intervals[i][0]<= newInterval[1]):
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
        merged.append(newInterval)
        print(merged)
        # Append remaining intervals
        while i<n:
            merged.append(intervals[i])
            i+=1
        print(merged)
        return merged


obj = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
obj.insert(intervals,newInterval)
