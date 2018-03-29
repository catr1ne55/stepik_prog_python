numbers = input()
t = [int(i) for i in str(numbers)]
s1 = sum(t[:3])
s2 = sum(t[3:])
if s1 == s2:
    print('Счастливый')
else:
    print('Обычный')