x=str(input("Enter a string :"))
firstchar=x[0]
x=x.replace(firstchar,'$')
x=firstchar+x[1:]
print(x)