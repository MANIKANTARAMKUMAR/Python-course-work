'''try:
    file=open('python.txt','a+')
except Exception as e:
    print(f"error {e}")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    file.write("file operations")
    file.seek(0)
    print(file.read())
    file.seek(0)'''
with open('python.txt','r') as file:
    print(file.read())