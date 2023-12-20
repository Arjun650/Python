def secondLargest(l):
    length = len(l)
    print(l[length-2])
    

List = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    ele = int(input(f"Enter the element {i+1}: "))
    List.append(ele)
    
secondLargest(List)
    