#Wap to print largest among three numbers
a=int(input("enter 1st numbers"))
b=int(input("enter 2st numbers"))
c=int(input("enter 3st numbers"))

if a>b and a>c:
    print (f"{a} is greatest")
elif b>a and b>c:
    print (f"{b} is greatest")
elif c>a and c>b :
    print (f"{c} is greatest")
else:
    print('conditon not matched')