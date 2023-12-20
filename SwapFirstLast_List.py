# Given a list, write a Python program to swap first and last element of the list.

List = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    ele = int(input(f"Enter the element {i+1}: "))
    List.append(ele)
print("The list is " , List)
t = List[0]
List[0] = List[n-1]
List[n-1] = t
print("The new list is " , List)