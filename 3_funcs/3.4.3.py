text = open("dataset_3363_4.txt", 'r')
strings = text.read().splitlines()
text.close()
l = len(strings)
smath, sphys, srus = 0, 0, 0
for s in strings:
    name, math, phys, rus = s.split(';')
    math = int(math)
    phys = int(phys)
    rus = int(rus)
    smath += math
    sphys += phys
    srus += rus
    sr = (math + phys + rus) / 3
    print(round(sr, 9))
print(round(smath/l, 9), round(sphys/l, 9), round(srus/l, 9))