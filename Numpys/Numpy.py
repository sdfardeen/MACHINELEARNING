import numpy as np
import array

a = np.full((10,10),6)
print(a)
# np.full() is creating a new array with the shaope of (10,10) of element 6.

a1 = np.zeros((9,2))
print(a1)
# we're creating a new array with only zeros
print(np.full_like(a1,10))
# by np.full_like() we're replacing the elements in given array

a2 = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(a2)
# creating a new array

a21 = a2[[0, 1, 2, 3], [3, 2, 1, 0]]
print(a21)
# working as (0,3),(1,2),(2,1),(3,0) as indices/index positions

A = np.array([[0, 1, 2, 3, 4],
      [5, 6, 7, 8, 9],
      [10, 11, 12, 13, 14]])
B = np.array([[10, 11, 12, 13, 14],
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9]])
print(A+B)
# here we're adding two arrays

A1 = np.array([[1, 2],
             [3, 4]])
B1 = np.array([[5, 6],
             [7, 8]])
print(A1.dot(B1))

# here it's working on matrix multiplication which means
# [[(1*5)+(2*7)=19,  (1*6)+(2*8)=22],
#  [(3*5)+(4*7)=43,  (3*6)+(4*8)=50]]
print(np.sqrt(A1))
# printing the square root values of A1

ar = array.array('i', [1, 2, 3])
for i in range(0, 3):
    print(ar[i])

arr = np.arange(0, 15, 2)
print(arr)
# printing the range of 0 to 15

arr = np.arange(0, 15, 2)
print(arr)
# here in np.arange() step is mandatory to print the indices

new_arr = arr[np.array([0, 3, 6])]
print(new_arr)
# printing indices of arr

na = np.arange(20)
print(na)
print(na[-11:19:1])
# slicing syntax(start:stop:step)

a = np.array([10, 40, 80, 50, 100])
print(a)
print(a[a > 15])
# printing the elements which are greater than 15 in the array of "a"

Np = np.array([[5, 5],[4, 5],[16, 4]])
N_p = Np.sum(-1)
print(Np[N_p % 10 == 0])
# printing those which are divisible by 10, those will be printed
print(N_p)
# printing the elements after adding the elements

dtyp = np.array(([19]))
print(dtyp.dtype)
# to know the data type of given element

nd_iter = np.array([1,2,3,4,5])
print("Original array:", nd_iter)
for i in np.nditer(nd_iter):
    print(i)
# output:
#       Original array: 1
#                       2
#                       3
#                       4
#                       5
