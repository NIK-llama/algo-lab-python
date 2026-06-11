def ternarySearch(l,r,x,arr):
    while l <= r:
        mid1 = l + (r-l) // 3
        mid2 = r - (r- l) // 3

        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif arr[mid1] > x:
            return ternarySearch(l,mid1-1,x,arr)
        elif arr[mid2] < x:
            return ternarySearch(mid2+1,r,x,arr)
        else:
            return ternarySearch(mid1+1,mid2-1 ,x,arr)
    return -1


## Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = 0
r = len(arr) - 1
x = 10

## function calling
result = ternarySearch(l, r, x, arr)

print("Searching element is present at index:", result)