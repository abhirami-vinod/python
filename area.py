print("Rectangle:")
l=int(input("Enter the length :"))
b=int(input("Enter the breadth :"))
c=lambda x,y:x*y
print("Area of rectangle :"+str(c(l,b)))
print("Square:")
a=int(input("Enter the side of square :"))
c=lambda x:x*x
print("Area of square :"+str(c(a)))
print("Triangle:")
b=int(input("Enter the base :"))
h=int(input("Enter the height :"))
c=lambda x,y:.5*b*h
print("Area of triangle :"+str(c(b,h)))
