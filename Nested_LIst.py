# Write a function called list_add that takes a list of lists of integers and adds up the elements from all of the nested lists.
# Sample Input:
#  t = [[1, 2], [3], [4, 5, 6]]
# output:
# 21

t = [[1, 2], [3], [4, 5, 6]]
def Add():
    sum = 0 
    for i in range (len(t)):
        for j in range (len(t[i])):
            sum += t[i][j]
    return sum
    

print("The sum of the elements of list is ",Add())