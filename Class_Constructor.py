class Student:
    def __init__(self):
       self.n = int(input("Enter the number: "))
        
    def check(self):
        if(self.n % 2 == 0):
            print("Even Number.")
        else:
            print("Odd Number.")
    
s1 = Student()
s1.check()