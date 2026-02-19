class file_operations:
    def create_file(self,file_path):
        try:
            with open(file_path,'x') as file:
                print(f"file {file_path} created successfully.")
        except FileExistsError:
            print(f"file {file_path} already exists.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("file creation operation completed.\n")

    def read_file(self,file_path):
        try:
            with open(file_path,'r') as file:
                content=file.read()
                print("file content:")
                print(content)
        except FileNotFoundError:
            print(f"file {file_path} not found.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("file read operation completed.\n")
    def write_file(self,file_path,data):
        try:
            with open(file_path,'w') as file:
                file.write(data)
                print(f"data written to {file_path} successfully.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("file write operation completed.\n")
    def append_file(self,file_path,data):
        try:
            with open(file_path,'a') as file:
                file.write(data)
                print(f"data appended to {file_path} successfully.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("file append operation completed.\n")
f=file_operations()
f.write_file("example.txt","hello world")
f.read_file("example.txt")
f.append_file("example.txt","\nwelcome to python programming")
f.read_file("example.txt")
f.create_file("example.txt")
f.create_file("newfile.txt")
f.read_file("nonexistent.txt")
