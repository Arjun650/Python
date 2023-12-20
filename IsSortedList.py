# def isSorted(l):
#        return l == sorted(l)

# List = [1,2,3,4,5]
# ch = isSorted(List)
# if ch:
#     print("Sorted List")
# else:
#     print("Not a sorted list")
    
    
    
    
def issort(l,reverse=False):
    list1 = sorted(l,reverse=reverse)
    return l == list1

List = [6,5,4,3]
List = [1,2,3,4]
# ch = issort(List,reverse=True)
List.sort(reverse=True)
print(List)
# if ch:
#     print("Sorted List in reverse order")
# else:
#     print("Not a sorted list in reverse order")