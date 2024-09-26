num1 = int(input("ENTER A NUMBER: "))
operation = input("OPERATION(+,-,*,/): ")
num2 = int(input("ENTER A NUMBER: "))

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("ERROR")