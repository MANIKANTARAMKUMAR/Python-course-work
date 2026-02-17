def square (x):
    return x * x

print (square(5))

square2 = lambda x: x * x
print(square2(5))


def even_odd (x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
print(even_odd(5))

even_odd2 = lambda x: 'even' if x % 2 == 0 else 'odd'
print(even_odd2(5))

#list of even and odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
even_odd_list = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
print(even_odd_list)

#print only nonzero numbers
numbers2 = [0,1,2,3,0,4,5,0,6,7,8,9,10]
nonzero_numbers = list(filter(lambda x: x != 0, numbers2))
print(nonzero_numbers)


#mapping
numbers3 = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x * x, numbers3))
print(squared_numbers)

#dictionary mapping
names = {'John': 25, 'Jane': 0, 'Doe': 35}
ages = list(map(lambda x: names[x], names))
print(ages)
#sorting a list of tuples

a={'apple': 2, 'banana': 3, 'orange': 1}
sorted_a = sorted(a.items(), key=lambda x: x[1])
print(sorted_a)


a={'apple': 2, 'banana': 3, 'orange': 1}
sorted_a = sorted(a.items(), key=lambda x: x[1],reverse=True)
print(sorted_a)


strings = ['hello', 'world', 'python']
uppercase_strings = list(map(lambda x: x.upper(), strings))
print(uppercase_strings)