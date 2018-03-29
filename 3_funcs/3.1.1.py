def f(x):
    if x <= -2:
        print(1 - (x + 2) ** 2)
    elif (x > -2) and (x <= 2):
        print(- x / 2)
    elif x > 2:
        print((x - 2) ** 2 + 1)

f(4.5)