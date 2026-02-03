import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("1-dim",arr1,sep='\n',end='\n\n')

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-dim",arr2,sep='\n',end='\n\n')

arr3 = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])
print("multi-dim",arr3,sep='\n')


zeros = np.zeros((4, 5))
print(zeros)


ones = np.ones((3, 4))
print(ones)


identity = np.eye(4)
print(identity)


full_array = np.full((10, 3),"Null")
print(full_array)

range_arr = np.arange(1,100,2)
print(range_arr)

lin_space = np.linspace(0, 10, 5)
print(lin_space)

rand_int = np.random.randint(1, 3, (4, 4))
print(rand_int)

rand_int = np.random.randint(20, 26)
print(rand_int)