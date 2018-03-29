a = int(input())
b = int(input())
s = 0
k = 0
if a % 3 == 2:
    a += 1
elif a % 3 == -2:
    a += 2
elif a % 3 == 1:
    a += 2
elif a % 3 == -1:
    a += 1
for i in range(a, b + 1, 3):
    if i % 3 == 0:
        s += i
        k += 1
print(s/k)