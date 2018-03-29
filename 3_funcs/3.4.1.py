letters = input()
for i in range(len(letters)):
    cur = letters[i]
    num = ""
    if not cur.isdigit():
        while i < len(letters) - 1:
            nl = letters[i + 1]
            if nl.isdigit():
                num += nl
                i += 1
            else:
                break
        num = int(num)
        for j in range(num):
            print(cur, end='')

