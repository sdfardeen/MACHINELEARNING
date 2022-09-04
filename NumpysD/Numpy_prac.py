import numpy as np
import array

a = np.full((10, 10), 6)
print(a)
# np.full() is creating a new array with the shaope of (10,10) of element 6.

a1 = np.zeros((9, 2))
print(a1)
# we're creating a new array with only zeros
print(np.full_like(a1, 10))
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
print(A + B)
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

Np = np.array([[5, 5], [4, 5], [16, 4]])
N_p = Np.sum(-1)
print(Np[N_p % 10 == 0])
# printing those which are divisible by 10, those will be printed
print(N_p)
# printing the elements after adding the elements

dtyp = np.array(([19]))
print(dtyp.dtype)
# to know the data type of given element

nd_iter = np.array([1, 2, 3, 4, 5])
print("Original array:", nd_iter)
for i in np.nditer(nd_iter):
    print(i)
# output:
#       Original array: 1
#                       2
#                       3
#                       4
#                       5

re = np.arange(20)
re = re.reshape(5, 4)
print(re)
# printing the given range of elements iin the shape of (5,4)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

sliced_arr = arr[:2, ::2]
print(sliced_arr)
# slicing the elements

for i in np.nditer(arr, order='F'):
    print(i)
# printing every element in a single column using np.nditer()

print(np.char.lower(['SYED', 'FARDEEN']))
# printing all upper case char to lower case char

print(np.char.split('Iam Fardeen'))
# splitting a sentence in seperate words
print(np.char.split('Iam, Fardeen', sep=","))
print(np.char.join('.', 'fardeen'))
# joining both words by its 2nd word for each char of that word

so = np.array([[12, 15], [10, 1]])
so1 = np.sort(so, axis=0)
print(so1)
# sorting the elements along the axis 0

so2 = np.sort(so, axis=-1)
print(so2)
# sorting elements in axis -1

rand = np.random.randint(low=0, high=3, size=5)
print(rand)
# printing random integers
