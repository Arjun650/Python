n = int(input("Enter the number of terms: "))

for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")