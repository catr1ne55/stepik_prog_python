a = []
while True:
    s = input()
    if s != "end":
        a.append(list(int(i) for i in s.split()))
    else:
        break
m = len(a)
n = len(a[0])
for i in range(m):
    for j in range(n):
        print(a[i - 1][j] + a[i - m + 1][j] + a[i][j - 1] +a[i][j - n + 1], end=" ")
    print()