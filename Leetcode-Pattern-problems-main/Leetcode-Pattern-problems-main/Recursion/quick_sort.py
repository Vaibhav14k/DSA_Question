
def partition(arr,s,e):
    pivot = arr[s]
    print(arr)
    count = 0
    for i in  range(s+1,e+1):
        if pivot>=arr[i]:
            count+=1
    pivotIndex = s + count 
    arr[pivotIndex],arr[s] = arr[s],arr[pivotIndex]
    i,j = s,e
    while i<pivotIndex and j>pivotIndex:
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return pivotIndex



def quicksort(arr,s,e):
    if s>=e :
        return 
    mid = partition(arr,s,e)
    quicksort(arr,s,mid-1)
    quicksort(arr,mid+1,e)

arr = [24, 5, 12, 90, 32, 8,5,5,8,8]
quicksort(arr, 0, len(arr) - 1)
# print(arr)