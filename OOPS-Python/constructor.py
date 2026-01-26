class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("Adding New Student in DB")

s1 = Student("Bhavy Sharma")
print(s1.name)
s2 = Student("Coder Shab")
print(s2.name)  