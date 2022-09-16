a=input()
s=int(input())
b1=0
bonus=0
if(s<10000):
    b1=s/2
if a=='A':
    bonus = s*0.05
    print("Bonus",bonus)
if a=='B':
    bonus = s*0.1
    print("Bonus ",bonus)
print("TOtal to be paid ",s+bonus+b1)
