class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

class Solution:    
    
    def fractionalknapsack(self, w,arr,n):
        arr.sort(key=lambda x:(x.value/x.weight), reverse=True)
        total = 0.0
        for item in arr:
            if  item.weight <= w:
                w -= item.weight
                total += item.value
            else:
                total += w * (item.value/item.weight)
                break
        return total

obj = Solution()
n = 3
w = 50
values = [60,100,120]
weights = [10,20,30]
items = [Item(values[i], weights[i]) for i in range(len(values))]
print(obj.fractionalknapsack(w,items,n))