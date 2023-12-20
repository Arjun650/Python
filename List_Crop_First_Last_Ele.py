# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. 
# Input:
#  t = [1, 2, 3, 4]
# output:
# [2, 3]

t = []
n = int(input("Enter the size of list: "))
for i in range (n):
    ele = int(input(f"Enter the element {i+1}: "))
    t.append(ele)
print("The list before trim is ", t)
print("The list after trim is ", t[1:n-1])