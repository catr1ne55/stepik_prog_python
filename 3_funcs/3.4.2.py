text = open("dataset_3363_3.txt", 'r')
strings = text.read().replace('\n', ' ').lower().split()
text.close()
# strings = input().split(" ")
sets = set(strings)
maxw = {}
for i in sets:
    cur = strings.count(i)
    maxw.setdefault(i, cur)
w = max(maxw.values())
maxv = []
for word, count in maxw.items():
    if count == w:
        maxv.append(word)
maxv = sorted(maxv)
print(maxv[0], w)