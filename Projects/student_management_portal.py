class LowAttendenceError(Exception):
    pass
class Student:
    def __init__(self):
        self.students={"john":[80,90,70]}
    def calculate_average(self,marks):
        try:
            total=sum(marks)
            average=total/len(marks)
            if average<50:
                raise LowAttendenceError("student has low attendence")
            print(f"average marks :{average}")
        except ZeroDivisionError:
            print("marks list is empty")
        except LowAttendenceError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("average calculation completed.\n")
    def check_marks(self,name):
        try:
            marks=self.students[name]
            self.calculate_average(marks)
        except KeyError:
            print(f"student {name} not found.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("marks check completed.\n")
    def check_attendence(self,name,attendence):
        try:
            if attendence<75:
                raise LowAttendenceError("student has low attendence")
            print(f"{name} has good attendence.")
        except LowAttendenceError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("attendence check completed.\n")

    def check_performance(self,name,marks,attendence):
        try:
            self.check_marks(name)
            self.check_attendence(name,attendence)
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("performance check completed.\n")

    def add_student(self,name,marks):
        try:
            if name in self.students:
                raise ValueError(f"student {name} already exists.")
            self.students[name]=marks
            print(f"student {name} added successfully.")
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("add student operation completed.\n")

    def read_student_data(self,file_path):
        try:
            with open(file_path,"r") as file:
                for line in file:
                    name,marks= line.strip().split(":")
                    marks_list=list(map(int,marks.split(",")))
                    self.students[name]=marks_list
        except FileNotFoundError:
            print(f"file {file_path} not found.")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("student data read completed.\n")

    def write_student_data(self,file_path):
        try:
            with open(file_path,"w") as file:
                for name,marks in self.students.items():
                    marks_str=",".join(map(str,marks))
                    file.write(f"{name}:{marks_str}\n")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("student data write completed.\n")

    def add_student_infile(self,file_path,name,marks):
        try:
            with open(file_path,"a") as file:
                marks_str=",".join(map(str,marks))
                file.write(f"{name}:{marks_str}\n")
        except Exception as e:
            print("An unexpected error occurred:", e)
        finally:
            print("add student to file operation completed.\n")

s=Student()
s.add_student("doe",[50,60,49])
s.check_marks("john")
s.check_marks("doe")
s.check_attendence("john",80)
s.check_attendence("doe",60)
s.check_performance("john",s.students["john"],80)
s.check_performance("doe",s.students["doe"],60)
s.read_student_data("students.txt")
s.write_student_data("students.txt")
s.add_student_infile("students.txt","alice",[85,90,95])
