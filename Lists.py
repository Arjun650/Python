list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']

list3 = [list1,list2]

# print(list1)
# print(list2)
# print(list3)

list1.append(6)
list2.pop(2)

print(list2)
print(list1)

list1.insert(0,8)
print(list1)

list1.remove(8)
print(list1)

list1.extend([2,3,4,5])
print(list1)

list1.sort()
print(list1)


# list1.len()
print(len(list1))

list1[2:4] = [10,11]
print(list1)