class Computer:
    def getData(self):
        self.st = str(input("Enter the type of computer: "))
        
    def disp(self):
        print("The type of computer is " + self.st)
        
#main Function
c1 = Computer()
c1.getData()
c1.disp()


# Computer.getData(c1)
# Computer.disp(c1)