from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        counter = defaultdict(int)
        for i in bills :
            print(counter)
            counter[i] = counter.get(i,0) + 1
            if i == 10 :
                if counter[5] < 1:
                    return False
                counter[5] -= 1  
            elif i==20 :
                if counter[10] >= 1 and counter[5] >= 1:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
        print(counter) 
        return True

obj = Solution()
bills = [5,5,5,10,20]
bills = [5,5,10,10,20]
bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(obj.lemonadeChange(bills))  