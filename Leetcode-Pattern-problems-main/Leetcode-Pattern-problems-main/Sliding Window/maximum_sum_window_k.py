def maximum_sum_of_k_size_subarray(arr,k)->int:
    max_sum=0
    window_sum=0
    start=0
    for i in range(k):
        window_sum+=arr[i]

    max_sum=window_sum

    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[start]
        max_sum = max(max_sum, window_sum)
        start+=1
    
    print("maximum sum-->",max_sum)


# arr = [2,1,5,1,3,2]
# k = 3
# maximum_sum_of_k_size_subarray(arr,k)

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for i in range(t):
        k = int(input("Enter the window size: "))
        arr = list(map(int,input().split()))
        maximum_sum_of_k_size_subarray(arr,k)