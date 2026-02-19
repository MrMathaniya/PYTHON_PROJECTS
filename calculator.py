op=(input("Enter operation{1:+, 2:-, 3:*, 4:/}:"))

if op not in("1","2","3","4"):
    print("Invalid operation entered,stopping!")
    exit()
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if op=="1":
     print("sum:",a+b)
elif op=="2":
     print("Difference:",a-b)
elif op=="3":
     print("product:",a*b)
elif op=="4":
    if b==0:
        print("Cannot divide by zero!")
    else:
     print("quotient:",a/b)