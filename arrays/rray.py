from array import array

arr = array('i',[1,2,3,4,5,6,7,8,9])

# for i in range(0,len(arr)):
#     print(arr[i], end=" ")

# print("\n")

# for x in arr:
#     print(x,end=" ")

# print("\n")

# print(arr.typecode)

# arr.reverse()
# for i in arr:
#     print(i,end=" ")

# arr.insert(0,50)
# arr.append(90)
# arr[0] = 0
# for i in arr:
#     print(i,end=" ")

# copy_arr = array(arr.typecode,(x*2 for x in arr))
# copy_arr.pop()
# copy_arr.remove(4)
# for i in copy_arr:
#     print(i,end=" ")

# arr1 = arr[2:5]
# arr2 = arr[2:-3]
# arr3 = arr[::-1]
# for i in arr3:
#     print(i,end=" ")

# arr4 = array('i', [])
# n = int(input("Enter a number: "))

# for i in range(0,n):
#     arr4.append(int(input("Enter next input: ")))

# for i in arr4:
#     print(i,end=" ")

# i = arr.index(3)
# print(i)

### ----- NUMPY ------ ####
import numpy as np

# arrr = np.array([1,2,3,4,5], int)
# for i in arrr:
#     print(i,end=" ")

# arrr1 = np.linspace(10, 20, 6)
# for i in arrr1:
#     print(i,end=" ")

# arrr2 = np.arange(10, 20, 2)
# for i in arrr2:
#     print(i,end=" ")

# arrr3 = np.ones(10)
# for i in arrr3:
#     print(i,end=" ")

# arrr4 = np.full(10,5)
# for i in arrr4:
#     print(i,end=" ")

# zero = np.array(10)
# print(zero)
# one= np.array([1,2,3])
# print(one)

# two = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(two)

three = np.array([[[1,2,3], [4,5,6]], [[3,0,6], [7,8,9]]])
print(three)



