def binarySearch(arr, low, high, x) :
    while low <= high :
        mid = low + (high - low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr,mid+1,high,x)
        else:
            return binarySearch(arr,low,mid-1,x)
    return -1
         



arr = [2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x = 59
low = 0
high = len(arr) - 1

## Function call
result = binarySearch(arr,low, high, x)
print("Searching element is present at the index", result)