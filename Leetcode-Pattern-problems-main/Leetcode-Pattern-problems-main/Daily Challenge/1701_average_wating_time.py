class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        total = customers[0][0]
        i = 0
        n = len(customers)
        current = 0
        total = 0
        for arrival,time in customers:
            if current < arrival:
                current = arrival
            finish_time = current + time 
            waiting = finish_time - arrival
            total += waiting
            current = finish_time
        return total/n


obj = Solution()
customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
print(obj.averageWaitingTime(customers))
