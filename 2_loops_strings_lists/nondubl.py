nums = [int(i) for i in input().split(' ')]
setn = list(set(nums))
for i in setn:
    if nums.count(i) > 1:
        print(i, end=' ')