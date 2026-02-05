import numpy as np


"""arr1 =np.array([1, 2, 3, 4, 5])
print("1-dim",arr1,sep='\n',end='\n\n')

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-dim",arr2,sep='\n',end='\n\n')

arr3 = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
print("multi-dim",arr3,sep='\n')
"""
'''
zeros = np.zeros((4, 5))
print(zeros)

ones= np.ones((2,3))
print(ones)

identify =np.eye(4)
print(identify)

full_array=np.full((11,5),7)
print(full_array)
'''
'''
range_arr = np.arange(1,100,2)
print(range_arr)

linspace_arr = np.linspace(0,1,5)
print(linspace_arr)

rand_int = np.random.randint(1,5,(4, 4))
print(rand_int)
'''
'''
rand_int = np.random.randint(20, 26)
print(rand_int)

rand_int=np.random.randint(80)
print(rand_int)

rand_float = np.random.rand(4, 4)
print(rand_float)

rand_choice = np.random.choice(['html','css','javascript','python','mysql'], 3)
print(rand_choice)

np.random.seed(10)

rand_arr = np.random.randint(6)
print(rand_arr)
'''

'''
arr = np.array([[1, 2], [4, 5],[6,7],[8,7],[1,2],[4,5]])


reshaped = arr.reshape(3,4)
print(reshaped)
print(arr.shape)


a=np.array([[1,2,3,4],[1,2,3,4]])
flattened = a.flatten()
print(flattened)

transposed = arr.T
print(transposed)

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[::2])
print(arr[::-1])

'''
'''
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(matrix[1,1])
print(matrix[0:3,0])


print(matrix[1:3, 1:3])
'''
arr =np.array([0,1,2,3,4,5,6,7,8,9,10,90])
print(arr+1)
print(arr*3)
print(arr**2)
print(np.sqrt(arr))
print(np.log(arr))
print(np.cos(arr))

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))



a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))
print(np.var(a))
print(np.std(a))


print(np.min(arr))
print(np.max(arr))

arr = np.array([1,2,3,4,5])
print(np.cumsum(arr))
print(np.cumprod(arr))

arr = np.array([10, 20, 30, 40, 50])

print(arr%20==0)
print(arr[arr%20==0])

arr = np.array([1,4,2,2,2,3,3,3,3])
sorted =np.sort(arr)
print(sorted)

unique_val=np.unique(arr)
print(unique_val)


arr = np.array([10, 20, 30])
view_arr = arr.view()
view_arr[0] = 100
print(arr,view_arr)

copy_arr = arr.copy()
copy_arr[0] = 200
print(arr,copy_arr)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))


print(np.linalg.det(A))

print(np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)

print(eigenvectors)

C = np.array([5, 11])
solution = np.linalg.solve(A, C)
print(solution)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))
print(vertical_stack)
print(horizontal_stack)

split_arr = np.split(np.array([1, 2, 3, 4, 5, 6]), 3)

print(split_arr)

