num1 = float(input())
num2 = float(input())
operation = input()
calc = 0
pred = (operation == '/' or operation == "mod" or operation == "div") and (num2 == 0)
if pred:
    print("Деление на 0!")
elif operation == '+':
    calc = num1 + num2
elif operation == '-':
    calc = num1 - num2
elif operation == '*':
    calc = num1 * num2
elif operation == '/':
    if num2 != 0:
        calc = num1 / num2
elif operation == "mod":
    if num2 != 0:
        calc = num1 % num2
elif operation == "div":
    if num2 != 0:
        calc = num1 // num2
elif operation == "pow":
    calc = pow(num1, num2)
if not pred:
    print(calc)