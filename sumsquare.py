l=[]
n=int(input("enter number of elements"))
for i in range (0,n):
    print("enter element:".format(i+1))
    ele=int(input())
    l.append(ele)
print("the entered list is:",l)
def sum_squares(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    l=[odd,even]
    return(l)
print(sum_squares(l))
