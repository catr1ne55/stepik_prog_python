def modify_list(l):
    l[:] = [x // 2 for x in l if x % 2 == 0]

y = [1, 2, 3, 4, 5]
modify_list(y)
print(y)