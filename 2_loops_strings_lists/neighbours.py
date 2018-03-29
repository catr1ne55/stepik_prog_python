l = [int(i) for i in input().split(" ")]
s = len(l)
if s == 1:
    print(l[0])
else:
    for i in range(s - 1):
        print(str(l[i - 1] + l[i + 1]), end=" ")
    print(str(l[s - 2] + l[0]))