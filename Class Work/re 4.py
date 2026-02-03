import random
import re as np


rand_int = np.random.randint(20, 26)
print(rand_int)

rand_int = np.random.randint(60)
print(rand_int)

rand_float = np.random.rand(4, 4)
print(rand_float)


rand_choice = np.random.choice(['html','css','javascript','python','mysql'], 3)
print(rand_choice)

np.random.seed(10)

rand_arr = np.random.randint(6)
print(rand_arr)

arr = np.array([[1, 2], [4, 5],[6,7],[8,7],[1,2],[4,5]])
print(arr.shape)
