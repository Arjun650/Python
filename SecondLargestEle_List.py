# Given a list of numbers, write a Python program to find the second largest number in the given list.

List = []
n = int(input("Enter the size of list: "))
for i in range(n):
    ele = int(input(f"Enter the element no.{i+1}: "))
    List.append(ele)
t = List[0]

for i in range(n):
    if(List[i] > t):
        t = List[i]
       
       