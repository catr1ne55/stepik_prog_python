#s = str(input()).lower()
#print(100 * (s.count("g") + s.count("c"))/ s.__len__())

s = str(input())
ns = ""
cur = s[0]
count = 0
i = 0
while i < len(s):
    while i < len(s) and cur == s[i]:
        count += 1
        i += 1
    ns += cur + str(count)
    if i < len(s):
        cur = s[i]
        count = 0
print(ns)