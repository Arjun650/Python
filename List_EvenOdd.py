# write a Python program to read a list L of n numbers and copy the Even and Odd numbers from L to  List1 and List2 respectively.

List = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    ele = int(input(f"Enter the element {i+1}: "))
    List.append(ele)
Even = []
Odd = []
for i in range(n):
    if(List[i]%2 == 0):
        Even.append(List[i])
    else:
        Odd.append(List[i])
print("The even numbers from the main list are ", Even)
print("The odd numbers from the main list are ", Odd)
