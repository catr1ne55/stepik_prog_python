n = int(input())
i = 0
j = 1
while i < n:
    for k in range(j):
        if i < n:
            print(j, end=' ')
            i += 1
        else:
            break
    j += 1
