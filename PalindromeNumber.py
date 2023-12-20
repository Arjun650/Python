n = int(input("Enter the number : "))
num = n
rev = 0
while(n > 0):
    rem = n % 10
    rev = rev * 10 + rem
    n //=10
if(rev == num):
    print(str(num)+ " is a palindrome number.")
else:
    print(str(num) + " is not a palindrome number.")