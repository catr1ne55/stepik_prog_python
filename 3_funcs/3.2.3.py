n = int(input())
dict = {}
for i in range(n):
    x = int(input())
    if x not in dict.keys():
        dict.setdefault(x, f(x))
    print(dict[x])