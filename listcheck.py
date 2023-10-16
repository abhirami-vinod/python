list1=[3,56,89,62,6]
list2=[6,54,25,7,90]
a=len(list1)
b=len(list2)
print("Lenth of list1 :",a)
print("Lenth of list2 :",b)
if a==b:
    print("Length of two list are same")
else:
    print("Lenth of two lists are not same")
c=sum(list1)
d=sum(list2)
print("Sum of list1:",c)
print("Sum of list2:",d)
if c==d:
    print("Sum of two lists are same")
else:
    print("Sum of two lists are not equal")
check=any(item in list1 for item in list2)
print("any value occure in both:",check)
