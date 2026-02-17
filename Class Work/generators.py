def display():
    yield 1
    yield 2
    yield 3
print(next(display()))

print(next(display()))