n = int(input())
i = 0
x, y = 0, 0
while i < n:
    dir, steps = input().split(" ")
    steps = int(steps)
    if dir == 'север':
        y += steps
    elif dir == 'запад':
        x -= steps
    elif dir == 'юг':
        y -= steps
    elif dir == 'восток':
        x += steps
    i += 1
print(x, y)