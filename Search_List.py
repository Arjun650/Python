# Write a python program to check if a particular element is present in list.

List = []
n = int(input("Enter the size of list: "))

for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    List.append(ele)  
key = int(input("Enter the key element to be searched: "))
count = 0
for i in range(n):
    if (key == List[i]):
        count = 1
        break
if (count == 1):
    print(key , "is present in the list.")
else:
    print(key , "is not present in the list.")