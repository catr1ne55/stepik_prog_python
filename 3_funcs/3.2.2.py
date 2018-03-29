str = [str(s).lower() for s in input().split(' ')]
dict = {}
for s in str:
    if s not in dict.keys():
        dict.setdefault(s, 1)
    else:
        dict[s] += 1
for key, value in dict.items():
    print(key, value)