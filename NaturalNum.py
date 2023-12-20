# write a program to find sum of first n natural numbers.
n=int(input("Enter the term: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first", n ,"natural numbers is",sum)