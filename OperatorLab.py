list1 = []
list2 = []
list3 = []
n1= int(input("Enter the size of first list: "))
n2= int(input("Enter the size of first list: "))
n3=int(input("Enter the size of first list: "))
for i in range(n1):
    ele = int(input(f"Enter the operand no.{i+1}: "))
    list1.append(ele)
  
for i in range(n2):
    ele = input(f"Enter the operator no.{i+1}: ")
    list2.append(ele)  

for i in range(n3):
    ele = int(input(f"Enter the operand no.{i+1}: "))
    list3.append(ele)
    
for i in range(n1):
    for j in range(n2):
        for k in range(n3):
            if list2[j] == '+':
                res = list1[i]+list3[k]
            elif list2[j]=='-':
                res = list1[i]-list3[k]
            elif list2[j] == '*':
                res = list1[i]*list3[k]
            elif list2[j]=='/':
                res = list1[i]/list3[k]
            else:
                print("Invalid operator")
                break
            print(f"{list1[i]} {list2[j]} {list3[k]} = {res}")