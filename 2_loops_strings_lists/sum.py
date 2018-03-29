s = int(input())
if s != 0:
    squad = s ** 2
    while s != 0:
        num = int(input())
        s += num
        squad += num ** 2
    print(squad)
else:
    print(0)