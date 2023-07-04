#Adding every number from the multiples
A=[]
b=[]
c=[]
for a in range(1,10):
    # print(a)
    if a%3==0:
        A.append(a)
    # print(A)
for a in range(1,10):
    # print(a)
    if a%5==0:
        b.append(a)
    # print(b)
for a in range(1,10):
    if a%6==0:
        c.append(a)
    # print(c)
list=A+b+c
set=set(list)
print(list, set)
total=sum(set)
print(total)