num=int(input("enter the number:"))
x=num
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
print("reverse of given number is",rev)
if x==rev:
    print("the num is palindrome")
else:
    print("the num is not palindrome")
