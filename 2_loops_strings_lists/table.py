a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(end='\t')
for k in range(c, d + 1):
    if k != d:
        print(k,end='\t')
    else:
        print(k)
for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        if j != d:
            print(i * j, end="\t")
        else:
            print(i * j)