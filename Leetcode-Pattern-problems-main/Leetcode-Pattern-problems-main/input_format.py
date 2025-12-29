t = int(input("Enter number of test cases: "))  # Number of test cases

for _ in range(t):
    n = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Read the array

    # Process the array as needed
    for num in arr:
        print(num, end=" ")
    print()